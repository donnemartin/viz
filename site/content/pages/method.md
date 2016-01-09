Title: Method
Date: 2016-01-01 06:00

## What Data is Tracked?

Although [GitHub Trending](https://github.com/trending) is a **great tool to discover up-and-coming projects**, it allows you to review **only one month** of data.  Third-party sites often show **all-time stats that are relatively static**, as they are dominated by well-established repos.

`gh-stats` is meant to supplement existing tools by **filtering only on the latest and most-starred repos** created within a specific timeframe.

For example, `viz` 2015 will only track repos created within the year 2015.

### Can We See Stats for Older Repos?

In the future, `viz` can be extended to track repos regardless of creation date.  [Feedback](https://github.com/donnemartin/gh-stats/issues) is welcome!

## How Do You Mine Data?

`viz` is powered by the [GitHub API](https://developer.github.com/v3/) and:

* `pandas` and `numpy` in an [IPython Notebook]() for data wrangling.
* [Google Maps API]() for location data.
* [Tableau Public]() for visualization.*

**Interested in visualizations in Python or R?  [Contribute]()!*

You can run similar queries manually through [GitHub Search](https://github.com/search).  To view the most-starred JavaScript repos created in 2015, run the following [query](https://github.com/search?utf8=%E2%9C%93&q=created%3A2015-01-01..2015-12-31+stars%3A%3E%3D100+language%3Ajavascript&type=Repositories&ref=searchresults):

    created:2015-01-01..2015-12-31 stars:>=100 language:javascript

To check stats for a user's or an org's repos that were created in 2015, run:

    created:2015-01-01..2015-12-31 stars:>=100 user:user_name

### Why Are My 2015 Manual Search Results Different from `viz` 2015?

* Star counts from the searches above will show data up to the time you performed the search.
* The `viz` 2015 stars were mined on `January 1, 2016, between 00:00 to 01:00 PDT`, and are preserved [here](https://github.com/donnemartin/viz/tree/master/language_stats/2015_frozen).

### Why Restrict Search Results to `stars:>=100`?

Only repos with `stars:>=100` are tracked to help filter GitHub's rapidly growing **30+ million** repositories and to keep within the [GitHub API rate limits](https://developer.github.com/v3/rate_limit/).  Further optimizations to the source code could reduce this restriction in the future.

Even with the `stars:>=100` restriction, `viz` 2015 contains data for 7059 of the most-starred repos created in 2015.

### Why Stars?

`viz` provides stats for repos, users, and orgs by stars.  Stars are by no means a perfect metric, yet they are a **simple and fairly effective measure of interest**.  For a more detailed discussion on measuring repo popularity, refer to the publication ["On the Popularity of GitHub Applications:
A Preliminary Note"](https://github.com/donnemartin/viz/blob/master/assets/gh-stats.pdf) which concludes:

>The number of stars of a system tends to correlate not only with the number of forks, but
also with its effective usage by other client applications, which reinforces the importance
of stars as a real measure of a system’s popularity.

In the future, other stats such as forks could be included, even for `viz` 2015.  Forks for the year 2015 were mined on `January 1, 2016, between 02:00 to 03:00 PDT`, and are preserved [here](https://github.com/donnemartin/viz/tree/master/language_stats/2015_with_forks).

## How Are Stats for Users and Orgs Calculated?

To provide star counts for users and orgs, `viz` groups repo stars by user or org.  Note the `stars:>=100` restriction still applies to counted repos.

## What Languages Are Tracked?

Stats available from the [Language Stats Index](#language-stats-index) are grouped based on repo language, as identified by [github/linguist](https://github.com/github/linguist).

`viz` tracks the most popular languages on GitHub plus the `Unknown` language option.  Data from each language is tallied to determine the [Overall Stats](#stats-index).

Don't see a popular language below?  Feel free to file a [request](https://github.com/donnemartin/viz/issues).

```
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
    'Unknown',
    'Overall',
]
```
