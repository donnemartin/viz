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


class User(object):
    """GitHub user.

    :type id: str
    :param id: The user's id or login name.

    :type name: str (optional)
    :param name: The user's name.

    :type type: str (optional)
    :param type: The user type: 'User' or 'Organization'.

    :type location: str (optional)
    :param location: The user's location.

    :type stars: int (optional)
    :param stars: The user's total repo stars.
    """

    def __init__(self, id, name=None, type=None, location=None, stars=None):
        self.id = id
        self.name = name
        self.type = type
        self.location = location
        self.stars = stars

    def __lt__(self, other):
        return self.stars < other.stars
