<p align="center">
  <img src="http://www.clker.com/cliparts/v/P/n/K/B/P/stars-md.png">
</p>

# gh-stats

> The **most-starred** GitHub repos **created in** 2015, the past six months, or the past three months.

`gh-stats` is a community project powered by the [GitHub API](https://developer.github.com/v3/) and is not affiliated with GitHub.

### [TLDR: Just show me the stats](#stats-index).

## Motivation

>Ever wonder what are the most-starred repos created in 2015?  The past six months?  The past three months?

Although [GitHub Trending](https://github.com/trending) is a **great tool to discover up-and-coming projects**, it allows you to review **only one month** of data.  Third-party sites often show **all-time stats that are relatively static**, as they are dominated by well-established repos.

`gh-stats` is meant to **supplement** existing tools by **filtering only on the most-starred repos created within a specific timeframe.**

*Why stars?  Check out the discussion in the the [method](#method) section.*

#### `gh-stats 2015`:

* Only tracks repos created within 2015.
* Provides stats for the entire 2015 year.

#### `gh-stats Six Months`, `Three Months`:

* Only tracks repos created within the past six months or three months.
* Updated regularly.
* *Coming soon.*

#### `gh-stats` is also:

* Hosted on GitHub, no need to visit a third-party site.
* Open source ([contributions](https://github.com/donnemartin/gh-stats/blob/master/CONTRIBUTING.md) are welcome).
* Under active development, providing more stats in the future ([feedback](https://github.com/donnemartin/gh-stats/issues) is  welcome).

## Method

>`gh-stats` only tracks repos created within a specified timeframe.  For example, `gh-stats 2015` will only track repos created within the year 2015.

`gh-stats` is powered by the [GitHub API](https://developer.github.com/v3/).

You can run similar queries through [GitHub Search](https://github.com/search).  To view the most-starred JavaScript repos created in 2015, you can run the following [query](https://github.com/search?utf8=%E2%9C%93&q=created%3A2015-01-01..2015-12-31+stars%3A%3E%3D100+language%3Ajavascript&type=Repositories&ref=searchresults):

    created:2015-01-01..2015-12-31 stars:>=100 language:javascript

To check stats for a user's or an org's repos that were created in 2015, run:

    created:2015-01-01..2015-12-31 stars:>=100 user:user_name

### Why Are My Search Results Different from `gh-stats 2015`?

* Star counts from the searches above will show data up to the time you performed the search.
* The `gh-stats 2015` stars were mined on January 1, 2016, between 00:00 to 01:00 PDT, and are preserved [here](https://github.com/donnemartin/gh-stats/tree/master/language_stats/2015_frozen).

### Why Restrict Searches to `stars:>=100`?

Only repos with **`stars:>=100`** are tracked to help filter GitHub's rapidly growing **30+ million** repositories and to keep within the [GitHub API rate limits](https://developer.github.com/v3/rate_limit/).  Further optimizations to the source code could reduce this restriction.

### Why Stars?

`gh-stats` provides stats for repos, users, and orgs by stars.  Stars are by no means a perfect metric, yet they are a simple and fairly effective measure of interest.

In the future, other stats such as forks could be included, even for `gh-stats 2015`.  Forks for the year 2015 were mined on January 1, 2016, between 02:00 to 03:00 PDT, and are preserved [here](https://github.com/donnemartin/gh-stats/tree/master/language_stats/2015_with_forks).

### How Are Stats for Users and Orgs Calculated?

To provide star counts for users and orgs, `gh-stats` groups repo stars by user or org.  Note the `stars:>=100` restriction still applies to counted repos.

### Which Languages Are Tracked?

Grouping in the [Language Stats Index](#language-index) is based on repo language as identified by [github/linguist](https://github.com/github/linguist).

`gh-stats` tracks the most popular languages on GitHub plus the `Unknown` language option.  Data from each language is tallied to determine the [overall stats](#stats-index).

```
self.languages = [
    'JavaScript',
    'Java',
    'Python',
    'Objective-C',
    'Swift',
    'Go',
    'PHP',
    'HTML',
    'CSS',
    'Ruby',
    'C++',
    'C',
    'C#',
    'Shell',
    'Scala',
    'Clojure',
    'Haskell',
    'CoffeeScript',
    'Lua',
    'R',
    'VimL',
    'Perl',
    'Unknown',
    'Overall',
]
```

## Stats Index

### Overall Stats

>The **100 Overall Most-Starred** Repos, Users, and Orgs.

* [Repos](https://github.com/donnemartin/gh-stats#most-starred-repos-overall)
* [Users](https://github.com/donnemartin/gh-stats#most-starred-users-overall)
* [Orgs](https://github.com/donnemartin/gh-stats#most-starred-orgs-overall)

### GOTO: [Language Stats Index](#language-index)

>Up to the **500 Most-Starred** Repos, Users, and Orgs, Organized by Language.
