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

import click

from .github_stats import GitHubStats


pass_github = click.make_pass_decorator(GitHubStats)


class GitHubStatsCli(object):
    """Provides access to GitHubStats from a CLI."""

    @click.group()
    @click.pass_context
    def cli(ctx):
        """Main entry point for GitHubCli.

        :type ctx: :class:`click.core.Context`
        :param ctx: Stores an instance of GitHubStats.
        """
        # Create a GitHubStats object and remember it as as the context object.
        # From this point onwards other commands can refer to it by using the
        # @pass_github decorator.
        ctx.obj = GitHubStats()

    @cli.command()
    @pass_github
    def rate_limit(github):
        """Outputs the rate limit.

        :type github_stats: :class:`GitHubStats`
        :param github_stats: Stores an instance of GitHubStats.
        """
        github.print_rate_limit()

    @cli.command('update_stats')
    @pass_github
    def update_stats(github_stats):
        """Updates the GitHub stats.

        See the README for more details.

        :type github_stats: :class:`GitHubStats`
        :param github_stats: Stores an instance of GitHubStats.
        """
        github_stats.update_stats()

    @cli.command('update_user_locations')
    @pass_github
    def update_user_locations(github_stats):
        """Updates the GitHub user location string with a geocoded location.

        :type github_stats: :class:`GitHubStats`
        :param github_stats: Stores an instance of GitHubStats.
        """
        github_stats.update_user_locations()
