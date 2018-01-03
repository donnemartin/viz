# coding: utf-8

# Copyright 2015 Donne Martin. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from operator import itemgetter
import os
import pickle
import re
import time

import click
import geocoder

from githubstats.lib.github import GitHub
from githubstats.repo import Repo
from githubstats.user import User


class UserGeocoder(object):
    """Geocodes a user based on the location field.

    TODO: This is a work-in-progress!

    :type cached_users: dict {user_id: :class:`githubstats.user.User`}
    :param cached_users: Cached users saved to disk to avoid always having
        to call the GitHub API.  This cache should be refreshed with fresh data
        from the GitHub API regularly.

    :type CFG_MAX_GEOCODES: int (constant)
    :param CFG_MAX_GEOCODES: The max number of locations to geocode.
        The Google Maps API has a limit of 2500 per day in the free tier.

    :type user_geocodes_map: dict {user_id: :class`geocoder.google.Google`}
    :param user_geocodes_map: Maps the user_id to a Google Geocode object.
    """

    CFG_MAX_GEOCODES = 2000

    def __init__(self, cached_users, user_geocodes_map):
        self.cached_users = cached_users
        self.user_geocodes_map = user_geocodes_map

    def generate_user_geocodes(self, csv_path, cache_path):
        """Generates geocodes for the user's provided location.

        :type csv_path: str
        :param csv_path: The user geocodes CSV path to update.

        :type cache_path: str
        :param cache_path: The user geocodes cache path to update.
        """
        count = 0
        for user_id, user in self.cached_users.items():
            if count >= self.CFG_MAX_GEOCODES:
                break
            if user_id in self.user_geocodes_map:
                continue
            if user.location is not None:
                count += 1
                geocode = geocoder.google(user.location)
                click.echo('geocoder status: {0} {1} '.format(str(count),
                                                              geocode.status))
                if geocode.status == 'OVER_QUERY_LIMIT':
                    click.secho('Geocode rate limit exceeded!', fg='red')
                    break
                self.user_geocodes_map[user_id] = geocode
            else:
                self.user_geocodes_map[user_id] = ''
        self.write_csv_users_geocodes(csv_path)
        self.save_user_geocodes_cache(cache_path)
        self.print_num_users_missing_geocodes()

    def print_num_users_missing_geocodes(self):
        """Prints the number of users with missing geocodes."""
        missing_count = 0
        for user_id, user in self.cached_users.items():
            if user_id in self.user_geocodes_map:
                continue
            if user.location is not None:
                missing_count += 1
        click.echo('Num users missing geocodes: {0}'.format(missing_count))

    def save_user_geocodes_cache(self, cache_path):
        """Saves the user_geocodes_map to cache.

        This avoids having to use up a Google Maps API call for user locations
        that have already been geocoded.

        :type cache_path: str
        :param cache_path: The user geocodes cache path to update.
        """
        with open(cache_path, 'wb') as users_geocodes_dat:
            pickle.dump(self.user_geocodes_map, users_geocodes_dat)

    def _write_csv_users_geocodes(self, users, users_dat):
        """Writes the users csv.

        Internal method, call write_csv_users instead.

        TODO: Refactor to use the built-in module `csv`.
        TODO: Refactor to combine with _write_csv_users.

        :type users: list
        :param users: The users.

        :type users_dat: :class:`_io.TextIOWrapper`
        :param users_dat: Handles writing the file.
        """
        count = 0
        for user_id, user in users.items():
            user_type = user.type
            name = user.name if user.name is not None else ''
            location = user.location if user.location is not None else ''
            location = location.replace('"', "'")
            try:
                lat_lng = self.user_geocodes_map[user.id].latlng
                lat = lat_lng[0]
                lng = lat_lng[1]
            except:
                # Geocoding can fail in many ways with the GitHub
                # location field being an optional, free-form text field.
                # For any failure, clear out the location fields.
                lat = ''
                lng = ''
                city = ''
                country = ''
            else:
                city = self.user_geocodes_map[user.id].city_long or ''
                country = self.user_geocodes_map[user.id].country_long or ''
            users_dat.write(
                user.id + ', ' + '"' +
                name + '", ' +
                user_type + ', ' + '"' +
                location + '", ' +
                str(lat) + ', ' +
                str(lng) + ', ' +
                city + ', ' +
                country + '\n')

    def write_csv_users_geocodes(self, csv_path):
        """Writes the users csv.

        :type csv_path: str
        :param csv_path: The user geocodes CSV path to update.
        """
        with open(csv_path, 'w') as user_geocodes_dat:
            user_geocodes_dat.write(
                'id, name, type, location, lat, long, city, country\n')
            self._write_csv_users_geocodes(self.cached_users, user_geocodes_dat)
