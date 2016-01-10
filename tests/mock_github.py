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

from github3 import null


class MockRepo(object):

    def __init__(self, full_name, stargazers_count,
                 forks_count, description, language=None):
        self.full_name = full_name
        self._stargazers_count = stargazers_count
        self._stars = stargazers_count
        self._forks_count = forks_count
        self._forks = forks_count
        self.description = description
        self.language = language

    def __lt__(self, other):
        return self.stars < other.stars

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @property
    def stargazers_count(self):
        return self._stargazers_count

    @stargazers_count.setter
    def stargazers_count(self, value):
        self._stargazers_count = value
        self._stars = value

    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, value):
        self._stargazers_count = value
        self._stars = value

    @property
    def forks_count(self):
        return self._forks_count

    @forks_count.setter
    def forks_count(self, value):
        self._forks_count = value
        self._forks = value

    @property
    def forks(self):
        return self._forks

    @forks.setter
    def forks(self, value):
        self._forks_count = value
        self._forks = value




class MockUser(object):

    def __init__(self, id, name, type, location=None, stars=0):
        self._id = id
        self._user_id = id
        self.name = name
        self.type = type
        self.location = location
        self.stars = stars

    def __lt__(self, other):
        return self.stars < other.stars

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
        self.user_id = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._id = value
        self.user_id = value


class MockResult(object):

    def __init__(self, repo):
        self._repository = repo

    @property
    def repository(self):
        return self._repository


class MockGitHubApi(object):

    def __init__(self, repos, users):
        self.repos = repos
        self.users = users
        self.ratelimit_remaining = 9000

    def repository(self, _, repo_name):
        for repo in self.repos:
            if repo.name == repo_name:
                return repo
        return null.NullObject()

    def search_repositories(self, query, sort=None):
        language = query.split(':')[-1]
        results = []
        for repo in self.repos:
            if repo.language is None:
                if language == 'unknown':
                    results.append(MockResult(repo))
            else:
                if language == repo.language.lower():
                    results.append(MockResult(repo))
        return results

    def user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None


class MockGitHub(object):

    def __init__(self, repos, users):
        self.api = MockGitHubApi(repos, users)
