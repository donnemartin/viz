# -*- coding: utf-8 -*-

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

import mock
import os
import unittest

from githubstats.github_stats import GitHubStats
from tests.mock_github import MockGitHub, MockRepo, MockUser
from tests.data.expected_output import expected_output


class GitHubStatsTest(unittest.TestCase):

    def setUp(self):
        self.repos = self.create_mock_repos()
        self.devs = self.create_mock_devs()
        self.orgs = self.create_mock_orgs()
        self.users = self.create_mock_users()
        self.user_repos_map = self.create_mock_user_repos_map()
        self.github = MockGitHub(self.repos, self.users)
        self.github_stats = GitHubStats(self.github)
        self.github_stats.languages = [
            'JavaScript',
            'Python',
            'Unknown',
            'Overall',
        ]

    def create_mock_repos(self):
        return [
            MockRepo('Google/foo', 250, 0, 'foo', 'Python'),
            MockRepo('Google/bar', 650, 0, 'bar', 'JavaScript'),
            MockRepo('Facebook/baz', 270, 0, 'baz', 'Python'),
            MockRepo('Facebook/qux', 550, 0, 'qux', 'JavaScript'),
            MockRepo('Facebook/foobar', 70, 0, 'foobar'),
            MockRepo('donnemartin/foobaz', 50, 0, 'foobaz', 'Python'),
            MockRepo('donnemartin/barfoo', 100, 0, 'barfoo', 'Python'),
            MockRepo('donnemartin/barbaz', 150, 0, 'barbaz'),
        ]

    def create_mock_devs(self):
        return [
            MockUser('donnemartin', 'Donne Martin', 'User', "Washington, D.C."),
        ]

    def create_mock_orgs(self):
        return [
            MockUser('Google', 'Google', 'Organization'),
            MockUser('Facebook', 'Facebook', 'Organization', 'Menlo Park'),
        ]

    def create_mock_users(self):
        users = []
        for dev in self.devs:
            users.append(dev)
        for org in self.orgs:
            users.append(org)
        return users

    def create_mock_user_repos_map(self):
        user_id_to_users_map = {}
        for repo in self.repos:
            user_id = repo.full_name.split('/')[0]
            if user_id in user_id_to_users_map:
                user_id_to_users_map[user_id].append(repo)
            else:
                user_id_to_users_map[user_id] = [repo]
        return user_id_to_users_map

    @mock.patch('githubstats.github_stats.click')
    @mock.patch('githubstats.github_stats.pickle')
    @mock.patch('githubstats.github_stats.time')
    @mock.patch('githubstats.github_stats.GitHubStats.write_output_files')
    def test_stats(self, mock_write, mock_time, mock_pickle, mock_click):
        self.github_stats.stats()
        assert mock_click.echo.mock_calls
        assert mock_pickle.mock_calls
        assert mock_time.sleep.mock_calls
        assert mock_write.mock_calls
        assert self.github_stats.output == expected_output
