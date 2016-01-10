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


class Repo(object):
    """GitHub repo.

    :type full_name: str
    :param full_name: The repos's full name (donnemartin/gh-stars).

    :type stars: int
    :param stars: The repos's total stars.

    :type forks: int
    :param forks: The repos's total forks.

    :type description: str
    :param description: The repos's description.

    :type language: str
    :param language: The repos's language.
    """

    def __init__(self, full_name, stars, forks, description, language):
        self.full_name = full_name
        self.stars = stars
        self.forks = forks
        self.description = description
        self.language = language

    def __lt__(self, other):
        return self.stars < other.stars
