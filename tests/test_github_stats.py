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

import csv
import mock
import unittest

from githubstats.github_stats import GitHubStats
from tests.mock_github import MockGitHub, MockRepo, MockUser
from tests.data.expected_output import expected_output
from tests.data.expected_csv import expected_csv


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
            MockUser('donnemartin', 'Donne Martin', 'User',
                     location="Washington, D.C.", stars=300),
        ]

    def create_mock_orgs(self):
        return [
            MockUser('Google', 'Google', 'Organization',
                     location=None, stars=900),
            MockUser('Facebook', 'Facebook', 'Organization',
                     'Menlo Park', stars=890),
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

    def verify_user(self, expected, results):
        for user_expected in expected:
            verified_user = False
            for user_result in results:
                if user_expected.id == user_result.id:
                    if user_expected.stars == user_result.stars:
                        print('ok')
                        verified_user = True
                    break
            assert verified_user

    def verify_results(self, expected_list, results_list):
        for expected in expected_list:
            verified = False
            for result in results_list:
                try:
                    expected_id = expected.id
                    result_id = result.id
                except:
                    expected_id = expected.full_name
                    result_id = result.full_name
                if expected_id == result_id:
                    if expected.stars == result.stars:
                        verified = True
                    break
            assert verified

    def read_csv(self, data_file_name):
        results = []
        file_path = self.github_stats.build_module_path(data_file_name)
        with open(file_path, 'r') as csv_dat:
            csv_reader = csv.reader(csv_dat)
            for line in csv_reader:
                results.append(''.join(line))
        return results

    def prep_collections(self):
        self.github_stats.cached_users = list(self.devs + self.orgs)
        self.github_stats.overall_repos = self.repos
        self.github_stats.overall_devs = self.devs
        self.github_stats.overall_orgs = self.orgs

    def test_caches(self):
        self.prep_collections()
        self.github_stats.write_caches()
        self.github_stats.load_caches()
        assert self.github_stats.overall_repos == self.repos
        assert self.github_stats.overall_devs == self.devs
        assert self.github_stats.overall_orgs == self.orgs

    def test_csvs(self):
        self.prep_collections()
        self.github_stats.write_csvs()
        results = self.read_csv('data/2017/repos-dump.csv')
        assert results == expected_csv

    @mock.patch('githubstats.github_stats.click')
    @mock.patch('githubstats.github_stats.time')
    def test_stats(self, mock_time, mock_click):
        self.github_stats.update_stats(use_user_cache=False)
        assert mock_click.echo.mock_calls
        assert mock_time.sleep.mock_calls
        self.verify_results(self.repos, self.github_stats.overall_repos)
        self.verify_results(self.devs, self.github_stats.overall_devs_grouped)
        self.verify_results(self.orgs, self.github_stats.overall_orgs_grouped)
        assert self.github_stats.output == expected_output
