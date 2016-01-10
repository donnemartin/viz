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

import unittest

from click.testing import CliRunner

from githubstats.github_stats_cli import GitHubStatsCli


class GitHubStatsCliTest(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()
        self.github_stats_cli = GitHubStatsCli()

    def test_cli(self):
        result = self.runner.invoke(self.github_stats_cli.cli)
        assert result.exit_code == 0
