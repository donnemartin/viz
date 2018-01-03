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

from collections import OrderedDict
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
from githubstats.user_geocoder import UserGeocoder


class GitHubStats(object):
    """Provides stats for users, orgs, and repos by stars.

    :type cached_users: dict {user_id: :class:`githubstats.user.User`}
    :param cached_users: Cached users saved to disk to avoid always having
        to call the GitHub API.  This cache should be refreshed with fresh data
        from the GitHub API regularly.

    :type CFG_USERS_PATH: str (constant)
    :param CFG_USERS_PATH: The users data directory path.

    :type CFG_SLEEP_TIME: int (constant)
    :param CFG_SLEEP_TIME: The time in seconds to sleep between generating
        stats for each language to avoid hitting the GitHub API rate limit.

    :type CFG_MAX_DESC: int (constant)
    :param CFG_MAX_DESC: The max description length before truncation.

    :type CFG_MAX_ITEMS: int (constant)
    :param CFG_MAX_ITEMS: The max number of items to display per section.

    :type CFG_MIN_STARS: int (constant)
    :param CFG_MIN_STARS: The min number of repo stars used as a cutoff to
        filter repos with GitHub search.

    :type github: :class:`githubstats.lib.GitHub`
    :param github: Provides integration with the GitHub API.

    :type languages: list
    :param languages: Programming languages tracked.

    :type overall_repos: list of :class:`githubstats.repo.Repo`
    :param overall_repos: Overall listing of repos.

    :type overall_devs: list of :class:`githubstats.user.User`
    :param overall_devs: Overall listing of devs.  Note duplicates can exist in
        this list if a dev has popular repos in different languages.

    :type overall_devs_grouped: list of :class:`githubstats.user.User`
    :param overall_devs_grouped: Overall listing of devs, grouped by language
        and sorted by stars.  Note duplicates can exist in this list if a dev
        has popular repos in different languages.

    :type overall_orgs: list of :class:`githubstats.user.User`
    :param overall_orgs: Overall listing of orgs.  Note duplicates can exist in
        this list if a dev has popular repos in different languages.

    :type overall_orgs_grouped: list of :class:`githubstats.user.User`
    :param overall_orgs_grouped: Overall listing of orgs, grouped by language
        and sorted by stars.  Note duplicates can exist in this list if a dev
        has popular repos in different languages.

    :type user_geocodes_map: dict {user_id: :class`geocoder.google.Google`}
    :param user_geocodes_map: Maps the user_id to a Google Geocode object.

    :type user_repos_map: dict
    :param user_repos_map: Maps the user_id and repos.
    """

    CFG_MAX_DESC = 50
    CFG_MAX_ITEMS = 500
    CFG_MIN_STARS = 100
    CFG_SLEEP_TIME = 5

    def __init__(self, github=None):
        self.github = github if github else GitHub()
        self.cached_users = {}
        self.overall_repos = []
        self.overall_devs = []
        self.overall_orgs = []
        self.overall_devs_grouped = []
        self.overall_orgs_grouped = []
        self.user_repos_map = {}
        self.user_geocodes_map = {}
        self.languages = [
            'JavaScript',
            'Java',
            'Objective-C',
            'Python',
            'Swift',
            'Go',
            'PHP',
            'C++',
            'C',
            'CSS',
            'HTML',
            'Ruby',
            'C#',
            'Shell',
            'Scala',
            'Clojure',
            'CoffeeScript',
            'Lua',
            'Haskell',
            'VimL',
            'R',
            'Perl',
            'Julia',
            'Rust',
            'Hack',
            'D',
            'TypeScript',
            'Unknown',
            'Overall',
        ]
        self.output = OrderedDict()
        for language in self.languages:
            self.output[language] = []
        self.output['Index'] = []
        self.CFG_USERS_PATH = self.build_module_path('data/2017/users')
        self.CFG_USERS_GEOCODES_PATH = self.build_module_path(
            'data/2017/users_geocodes')

    def build_module_path(self, path):
        """Builds the path relative to where the module is loaded.

        :type path: str
        :param path: The input pat to append to the module path.

        :rtype: str
        :return: The module path.
        """
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)

    def group_repos_by_user(self, users):
        """Groups repos in the given list by users.

        Example input:
            users[0] -> User(Google, 1000)
            users[1] -> User(Facebook, 2000)
            users[2] -> User(Google, 3000)
            users[3] -> User(Facebook, 4000)

        Example result:
            result[0] -> User(Facebook, 6000)
            result[1] -> User(Google, 4000)

        :type users: list
        :param users: A list of :class:`githubstats.user.User`.

        :rtype: list
        :return: A grouped sorted list of :class:`githubstats.user.User`.
        """
        user_stars_map = {}
        for item in users:
            if item.id in user_stars_map:
                user_stars_map[item.id].stars += item.stars
            else:
                user_stars_map[item.id] = User(item.id,
                                               item.name,
                                               item.type,
                                               item.location,
                                               item.stars)
        result_list_sorted = sorted(user_stars_map.items(),
                                    key=itemgetter(1),
                                    reverse=True)
        result = self.extract_list_column(result_list_sorted, column=1)
        return result

    def count_stars(self, language):
        """Counts the number of stars for the given language.

        Loop through all repos to determine:
            * Stars for each repo
            * Stars for each user

        To calculate stars for each user, sums up the stars for each repo
        that belongs to the user in the specified language.

        :type language: str
        :param language: The current language.

        :rtype: tuple
        :return: Tuple of (dict, list)
            dict: {key: user_id, value: :class:`githubstats.user.User}
            list: [:class:`githubstats.repo.Repo]
        """
        user_id_to_users_map = {}
        repos = []
        more_results = self.search_repos(
            user_id_to_users_map,
            repos,
            language)
        while more_results:
            self.sleep_for_rate_limiter(self.CFG_SLEEP_TIME*3)
            more_results = self.search_repos(
                user_id_to_users_map,
                repos,
                language,
                last_searched_repo=repos[len(repos)-1])
        return user_id_to_users_map, repos

    def extract_list_column(self, input_list, column):
        """Extracts the specified column in the input_list.

        Example:
            input_list = [['a', 'b'], ['c', 'd']]
            extract_list_column(input_list, 1) -> ['a', 'c']

        TODO: This would probably be faster with NumPy.

        :type input_list: list
        :param input_list: The input list to extract a column from.

        :type column: int
        :param column: The column index to extract.

        :rtype: list
        :return: The specified column.
        """
        result = []
        for item in input_list:
            result.append(item[column])
        return result

    def generate_overall_stats(self):
        """Generates the overall stats.

        The overall stats comprises all languages processed.
        """
        language = 'Overall'
        self.output_sorted_stars_per_repo(
            language, self.overall_repos, sort=True)
        self.overall_devs_grouped = self.group_repos_by_user(self.overall_devs)
        self.output_sorted_stars_per_user(language, self.overall_devs_grouped)
        self.overall_orgs_grouped = self.group_repos_by_user(self.overall_orgs)
        self.output_sorted_stars_per_org(language, self.overall_orgs_grouped)

    def generate_search_query(self, language,
                              creation_date_filter=None,
                              stars_filter=None):
        """Generates the GitHub search query.

        :type language: str
        :param language: The current language.

        :type creation_date_filter: str (optional)
        :param creation_date_filter: The repo creation date filter.

        :type stars_filter: str
        :param stars_filter: The stars filter.

        :rtype: str
        :return: The GitHub search query.
        """
        if creation_date_filter is None:
            creation_date_filter = 'created:>=2017-01-01'
        if stars_filter is None:
            stars_filter = 'stars:>=' + str(self.CFG_MIN_STARS)
        query = (creation_date_filter + ' ' + stars_filter +
                 ' language:' + language.lower())
        return query

    def generate_language_stats(self, language):
        """Generates the stats for the specified language.

        Outputs the following lists, sorted by stars:
            * Users
            * Orgs
            * Repos

        Also updates the overall stats.

        :type language: str
        :param language: The current language.
        """
        user_id_to_users_map, repos = self.count_stars(language)
        sorted_user_id_to_users = sorted(user_id_to_users_map.items(),
                                         key=itemgetter(1),
                                         reverse=True)
        # [('user_id0', User0), ('user_id1', User1] -> [User0, User1]
        sorted_users = self.extract_list_column(sorted_user_id_to_users,
                                                column=1)
        # Split up sorted_users, which contains both users and orgs
        devs, orgs = self.get_user_info(sorted_users)
        self.output_sorted_stars_per_repo(language, repos, sort=True)
        self.output_sorted_stars_per_user(language, devs)
        self.output_sorted_stars_per_org(language, orgs)
        self.overall_repos.extend(repos)
        self.overall_devs.extend(devs)
        self.overall_orgs.extend(orgs)

    def get_user_info(self, sorted_users):
        """Gets user info from the GitHubAPI.

        For each user in sorted_users, determines whether the user is
        a regular user or an organization.

        :type sorted_users: list
        :param sorted_users: Sorted list of users.

        :rtype: tuple of two lists
        :return: (first list, second list)
            First list: list of [:class:`githubstats.user.User`]
            Second list: list of [:class:`githubstats.repo.Repo`]
        """
        devs = []
        orgs = []
        self.print_rate_limit()
        for item in sorted_users:
            if item.id in self.cached_users:
                user = self.cached_users[item.id]
            else:
                user = self.github.api.user(item.id)
            if user.type == 'User':
                devs.append(User(item.id,
                                 user.name,
                                 user.type,
                                 user.location,
                                 item.stars))
            elif user.type == 'Organization':
                orgs.append(User(item.id,
                                 user.name,
                                 user.type,
                                 user.location,
                                 item.stars))
            self.print_rate_limit()
        return devs, orgs

    def load_cache(self, cache_path):
        """Loads the specified cached data.

        :type cache_path: str
        :param cache_path: The cache path.

        :rtype: dict
        :return: The cache data if exists, else an empty dict.
        """
        try:
            click.echo('Loading: ' + cache_path)
            with open(cache_path, 'rb') as data:
                return pickle.load(data)
        except (EOFError, FileNotFoundError):
            click.secho('Failed to load cache ' + cache_path, fg='red')
        return {}

    def load_caches(self):
        """Loads cached data."""
        click.echo('Loading caches...')
        self.cached_users = self.load_cache(self.CFG_USERS_PATH)
        self.user_geocodes_map = self.load_cache(self.CFG_USERS_GEOCODES_PATH)

    def output_index(self):
        """Outputs the language index.

        The language index includes links to users, orgs, and repos.
        """
        language_stats_loc = ('[gh-stats/language_stats/2017/](https://github'
                              '.com/donnemartin/gh-stats/tree/master/'
                              'language_stats/2017)')
        self.output['Index'].append('\n## Language Stats Index\n\n')
        self.output['Index'].append(
            '>Up to the **500 Most-Starred** Repos, Users, and Orgs, '
            'Organized by Language.\n\n'
            '*Due to the large number of [languages tracked](#which-languages'
            '-are-tracked) and the lengthy lists for each language, stats for '
            'each language can be found in ' + language_stats_loc + '.\n\n'
            'An index is provided below for convenience.*\n\n')
        self.output['Index'].append('| Language | 2017 |')
        self.output['Index'].append('|---|---|')
        for language in self.languages:
            base_url = ('https://github.com/donnemartin/gh-stats/blob/master/' +
                        'language_stats/2017/' + language.lower() + '.md')
            self.output['Index'].append(
                '| ' + language + ' | ' +
                '[Repos](' + base_url + '#most-starred-repos-' +
                language.lower() + ') - ' +
                '[Users](' + base_url + '#most-starred-users-' +
                language.lower() + ') - ' +
                '[Orgs](' + base_url + '#most-starred-orgs-' +
                language.lower() + ') |')

    def output_sorted_stars_per_org(self, language, orgs):
        """Outputs a list of orgs with their star count.

        List is sorted by star count, descending.
        Output of number of orgs is limited by CFG_MAX_ITEMS.

        :type language: str
        :param language: The current language.

        :type orgs: list
        :param orgs: List of orgs.
        """
        self.output[language].append(
            '\n## Most-Starred Orgs: ' + language + '\n')
        self.output[language].append('| | Org | Repos | Stars |')
        self.output[language].append('|---|---|---|---|')
        index = 1
        for org in orgs[:self.CFG_MAX_ITEMS]:
            self.output_user_results(language, org, index)
            index += 1

    def output_sorted_stars_per_repo(self, language,
                                     repos, sort=False):
        """Outputs a list of repos with their star count.

        List is sorted by star count, descending.
        Output of number of orgs is limited by CFG_MAX_ITEMS.

        :type language: str
        :param language: The current language.

        :type repos: list
        :param repos: List of repos.

        :type sort: boolean
        :param sort: Determines whether to sort the input list.
        """
        self.output[language].append(
            '\n## Most-Starred Repos: ' + language + '\n')
        if sort:
            repos = sorted(repos, reverse=True)
        self.output[language].append('| | Repo | Stars |')
        self.output[language].append('|---|---|---|')
        index = 1
        for repo in repos[:self.CFG_MAX_ITEMS]:
            description = repo.description if repo.description else ''
            description = description.strip()
            if len(description) > self.CFG_MAX_DESC:
                description = repo.description[0:self.CFG_MAX_DESC]
                description += '...'
            excludes = ['|', '\\n', '<', '>']
            for exclude in excludes:
                description = re.sub(exclude, '', description)
            if description != '':
                description = '<br/>' + description
            self.output[language].append(
                '| ' + str(index) + '. | [' +
                repo.full_name + '](https://github.com/' +
                repo.full_name + ') ' +
                description + ' | ' +
                str(repo.stars) + ' |')
            index += 1

    def output_sorted_stars_per_user(self, language, users):
        """Outputs a list of user with their star count.

        List is sorted by star count, descending.
        Output of number of orgs is limited by CFG_MAX_ITEMS.

        :type language: str
        :param language: The current language.

        :type users: list
        :param users: List of users.
        """
        self.output[language].append(
            '\n## Most-Starred Users: ' + language + '\n')
        self.output[language].append('| | User | Repos | Stars |')
        self.output[language].append('|---|---|---|---|')
        index = 1
        for user in users[:self.CFG_MAX_ITEMS]:
            self.output_user_results(language, user, index)
            index += 1

    def output_user_results(self, language, user, index):
        """Outputs the user, stars, and location in markdown format.

        :type language: str
        :param language: The current language.

        :type user: :class:`githubstats.user.User`
        :param user: The user.

        :type index: int
        :param index: The user's 1-based index position in the output table.
        """
        output_repos = ''
        repos = []
        for repo in self.user_repos_map[user.id]:
            repos.append(repo)
        sorted_repos = sorted(repos, reverse=True)
        for repo in sorted_repos:
            output_repos += ('[' + repo.full_name.split('/')[1] +
                             '](https://github.com/' + repo.full_name + ') ' +
                             ' (' + str(repo.stars) + ') <br/>')
        self.output[language].append(
            '| ' + str(index) + '. | [' +
            user.id + '](https://github.com/' +
            user.id + ') ' + ' | ' +
            output_repos + ' | ' +
            str(user.stars) + ' |')

    def print_rate_limit(self):
        """Prints the rate limit."""
        click.echo('Rate limit: ' + str(self.github.api.ratelimit_remaining))

    def search_repos(self, user_id_to_users_map, repos,
                     language, last_searched_repo=None):
        """Searches repos matching a query.

        Uses language and stars_filter to construct the query.

        :type user_id_to_users_map: dict, {str: :class:`githubstats.user.User`}
        :param user_id_to_users_map: Map of user ids to User.

        :type repos: list of :class:`githubstats.repo.Repo`
        :param repos: The list of repos.

        :type language: str
        :param language: The current language.

        :type last_searched_repo: :class:`githubstats.repo.Repo` (optional)
        :param last_searched_repo: The last repo encountered during a search,
            if any.  Used to resume searching if the list of results exceeds
            1000, the GitHub results search limit.

        :rtype: boolean
        :return: Determines if there are more results to search for.
        """
        stars_filter = None
        if last_searched_repo is not None:
            stars_max = last_searched_repo.stars
            stars_filter = ('stars:' + str(self.CFG_MIN_STARS) +
                            '..' + str(stars_max))
        query = self.generate_search_query(
            language, stars_filter=stars_filter)
        results = self.github.api.search_repositories(query, sort='stars')
        count = 0
        find_resume_point = True if last_searched_repo is not None else False
        try:
            for result in results:
                count += 1
                if find_resume_point and last_searched_repo.full_name != \
                        result.repository.full_name:
                    continue
                if find_resume_point and last_searched_repo.full_name == \
                        result.repository.full_name:
                    find_resume_point = False
                    continue
                if language == 'Unknown':
                    if result.repository.language is not None:
                        continue
                repo = Repo(result.repository.full_name,
                            result.repository.stargazers_count,
                            result.repository.forks_count,
                            result.repository.description,
                            result.repository.language)
                repos.append(repo)
                user_id = result.repository.full_name.split('/')[0]
                if user_id in user_id_to_users_map:
                    user_id_to_users_map[user_id].stars += \
                        result.repository.stargazers_count
                else:
                    user_id_to_users_map[user_id] = User(
                        user_id,
                        stars=result.repository.stargazers_count)
                if user_id in self.user_repos_map:
                    self.user_repos_map[user_id].append(repo)
                else:
                    self.user_repos_map[user_id] = [repo]
        except AttributeError:
            # github3.py sometimes throws the following during iteration:
            # AttributeError: 'NoneType' object has no attribute 'get'
            click.secho('count_stars caught AttributeError', fg='red')
        # The search_repositories call returns a maximum of 1000 elements
        return count == 1000

    def sleep_for_rate_limiter(self, sleep_duration):
        """Sleeps to avoid the GitHub rate limiter.

        :type sleep_duration: int
        :param sleep_duration: The sleep duration in seconds.
        """
        click.echo('Sleeping for ' + str(sleep_duration) +
                   ' second(s)...')
        time.sleep(sleep_duration)

    from .lib.debug_timer import timeit
    @timeit
    def update_stats(self, use_user_cache=True):
        """Updates the GitHub stats.

        Generates the index, stats per language, and overall stats.

        :type use_user_cache: boolean
        :param use_user_cache: Determines whether to use the existing user
            cache if it exists, or if the GitHub API should be called instead.
        """
        if use_user_cache:
            self.load_caches()
        click.echo('Printing index...')
        self.output_index()
        for language in self.languages:
            if language != 'Overall':
                click.echo('Generating stats for ' + language + '...')
                self.generate_language_stats(language)
                self.print_rate_limit()
                self.sleep_for_rate_limiter(self.CFG_SLEEP_TIME)
        if 'Overall' in self.languages:
            click.echo('Generating overall stats...')
            self.generate_overall_stats()
        self.print_rate_limit()
        self.write_output_files()

    def write_language_stats(self):
        """Writes the language_stats/ files."""
        for language in self.languages:
            file_path = 'language_stats/2017/' + language.lower() + '.md'
            with open(file_path, 'w+') as language_stats:
                if language == 'C#':
                    language_stats.write('# C-Sharp\n')
                else:
                    language_stats.write('# ' + language + '\n')
                for line in self.output[language]:
                    language_stats.write(line + '\n')
                for line in self.output['Index']:
                    language_stats.write(line + '\n')

    def write_output_files(self):
        """Writes the language stats and cached user file."""
        self.write_language_stats()
        self.write_caches()
        self.write_csvs()

    def write_caches(self):
        """Writes the user cached to data/2017/users"""
        self.cached_users = {}
        for dev in self.overall_devs:
            self.cached_users[dev.id] = dev
        for org in self.overall_orgs:
            self.cached_users[org.id] = org
        with open(self.CFG_USERS_PATH, 'wb') as users_dat:
            pickle.dump(self.cached_users, users_dat)

    def write_csvs(self):
        """Writes the repos and users csvs."""
        self.write_csv_repos('data/2017/repos-dump.csv')
        self.write_csv_users('data/2017/users-dump.csv')

    def write_csv_repos(self, data_file_name):
        """Writes the repos csv.

        TODO: Refactor to use the built-in module `csv`.

        :type data_file_name: str
        :param data_file_name: The resulting csv file name in the data folder.
            Example: 'data/2017/foo.csv'.
        """
        file_path = self.build_module_path(data_file_name)
        with open(file_path, 'w') as repos_dat:
            repos_dat.write('full_name, stars, forks, description, language\n')
            for repo in self.overall_repos:
                language = repo.language if repo.language is not None else ''
                desc = repo.description if repo.description is not None else ''
                desc = desc.replace('"', "'")
                repos_dat.write(
                    repo.full_name + ', ' +
                    str(repo.stars) + ', ' +
                    str(repo.forks) + ', ' + '"' +
                    desc + '", ' +
                    language + '\n')

    def _write_csv_users(self, users, users_dat, user_type):
        """Writes the users csv.

        Internal method, call write_csv_users instead.
        TODO: Refactor to use the built-in module `csv`.

        :type users: list
        :param users: The users.

        :type users_dat: :class:`_io.TextIOWrapper`
        :param users_dat: Handles writing the file.

        :type user_type: str
        :param user_type: 'User' or "Organization'
        """
        for user in users:
            name = user.name if user.name is not None else ''
            location = user.location if user.location is not None else ''
            location = location.replace('"', "'")
            users_dat.write(
                user.id + ', ' + '"' +
                name + '", ' +
                user_type + ', ' + '"' +
                location + '"' + '\n')

    def write_csv_users(self, data_file_name):
        """Writes the users csv.

        :type data_file_name: str
        :param data_file_name: The resulting csv file name in the data folder.
            Example: 'data/2017/foo.csv'.
        """
        file_path = self.build_module_path(data_file_name)
        with open(file_path, 'w') as users_dat:
            users_dat.write('id, name, type, location\n')
            self._write_csv_users(self.overall_devs,
                                  users_dat,
                                  'User')
            self._write_csv_users(self.overall_orgs,
                                  users_dat,
                                  'Organization')

    from .lib.debug_timer import timeit
    @timeit
    def update_user_locations(self, use_user_cache=True):
        """Updates the GitHub user location string with a geocoded location.

        TODO: This is a work-in-progress!

        :type use_user_cache: boolean
        :param use_user_cache: Determines whether to use the existing user
            cache if it exists, or if the GitHub API should be called instead.
        """
        if use_user_cache:
            self.load_caches()
        user_geocoder = UserGeocoder(self.cached_users, self.user_geocodes_map)
        csv_path = self.build_module_path('data/2017/user-geocodes-dump.csv')
        user_geocoder.generate_user_geocodes(csv_path,
                                             self.CFG_USERS_GEOCODES_PATH)
