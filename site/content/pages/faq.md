Title: FAQ
Date: 2016-01-01 06:00

## Why Did You Create Viz?

Viewing raw stats and tables only tell you **part of a story**.

![Imgur](http://i.imgur.com/yB9hv18.png)

`Viz` helps tell the rest of the story with **interactive visualizations** that are **continually updated**.

![Imgur](http://i.imgur.com/HBzXqrN.png)

## How Can We Help or Stay Up-To-Date with the Evolution of Viz?

`Viz` is just getting started.  [Contributions](https://www.github.com/donnemartin/viz/CONTRIBUTING) and [feedback]([Feedback](https://github.com/donnemartin/viz/issues)) are welcome!

Feel free to [follow](https://www.github.com/donnemartin), [star](https://github.com/donnemartin/viz/fork), [fork](https://github.com/donnemartin/viz/fork), and check back for updates.

<iframe src="https://ghbtns.com/github-btn.html?user=donnemartin&type=follow&count=true" frameborder="0" scrolling="0" width="145" height="20"></iframe>
<iframe id="gh-star" src="https://ghbtns.com/github-btn.html?user=donnemartin&amp;repo=viz&amp;type=watch&amp;count=false" allowtransparency="true" frameborder="0" scrolling="0" width="50" height="20"></iframe>
<iframe id="gh-fork" src="https://ghbtns.com/github-btn.html?user=donnemartin&amp;repo=viz&amp;type=fork" allowtransparency="true" frameborder="0" scrolling="0" width="53" height="20"></iframe>

## What Data is Tracked?

Although [GitHub Trending](https://github.com/trending) is a **great tool to discover up-and-coming projects**, it only allows you to review up to **one month** of data.  Third-party sites often show **all-time stats** that are **relatively static**, as they are dominated by well-established repos.

`Viz` is meant to supplement existing solutions by **filtering only on the latest and most-starred repos** created within a specific timeframe.

***For example, `Viz` 2015 will only track repos created within the year 2015.***

## Can We See Stats for Time Ranges Other than 2015?

For the initial launch, `Viz` provides stats for 2015.

Visualizations for 1-, 3-, and 6-month ranges are under development.  The data for each range will be continually updated to keep `Viz` fresh.

## Can We See Stats for 'Older' Repos?

In the future, `Viz` can be extended to track repos regardless of creation date.  [Feedback](https://github.com/donnemartin/viz/issues) is welcome!

## How Do You Mine Data?

`Viz` is powered by the [GitHub API](https://developer.github.com/v3/) through [github3.py](https://github.com/sigmavirus24/github3.py) and leverages the following:

* [`pandas`](https://github.com/pydata/pandas) and [`numpy`](https://github.com/numpy/numpy) with [IPython Notebook](https://github.com/ipython/ipython) for data wrangling.
* [Google Maps API](https://developers.google.com/maps/?hl=en) through [`geocoder`](https://github.com/DenisCarriere/geocoder) for location data.
* [Tableau Public](https://public.tableau.com/s/) for visualizations.*

**Interested in visualizations with Python or R?  [Contribute](https://www.github.com/donnemartin/viz/CONTRIBUTING)!*

You can manually run similar queries obtained from the GitHub API through [GitHub Search](https://github.com/search).  To view the most-starred JavaScript repos created in 2015, run the following [query](https://github.com/search?utf8=%E2%9C%93&q=created%3A2015-01-01..2015-12-31+stars%3A%3E%3D100+language%3Ajavascript&type=Repositories&ref=searchresults):

    created:2015-01-01..2015-12-31 stars:>=100 language:javascript

To check stats for a user's or an org's repos that were created in 2015, run:

    created:2015-01-01..2015-12-31 stars:>=100 user:user_name

## When Did You Mine the 2015 Data?

The `Viz` 2015 stats were mined on `January 1, 2016, between 00:00 to 01:00 PDT`, and are preserved [here](https://github.com/donnemartin/viz/tree/master/language_stats/2015_frozen).

## Where Can We Find the Data?

* [Data](https://github.com/donnemartin/viz/tree/master/githubstats/data)
* [Data Tables](https://github.com/donnemartin/viz/tree/master/language_stats)
* [Tableau Workbooks](https://github.com/donnemartin/viz/tree/master/viz)

## Why Are My 2015 Manual Search Results Different from `Viz` 2015?

Star counts from the searches above will show data up to the time you performed the search.

## Why Restrict Search Results to `stars:>=100` for `Viz` 2015?

Only repos with `stars:>=100` are tracked to help filter GitHub's rapidly growing **30+ million** repositories and to keep within the [GitHub API rate limits](https://developer.github.com/v3/rate_limit/).

`Viz` 1-, 3-, and 6-month might loosen this restriction as there should be less repos to analyze.  [Google BigQuery](https://cloud.google.com/bigquery/) along with [GitHub Archive](https://www.githubarchive.org/) could also supplement the GitHub API.

## Why Stars?

`Viz` provides stats for repos, users, and orgs by stars (and in some cases, forks).  **Stars are by no means a perfect metric**, yet they are a **simple and fairly effective measure of interest**.  For a more detailed discussion on measuring repo popularity, check out ["On the Popularity of GitHub Applications:
 A Preliminary Note"](https://github.com/donnemartin/viz/blob/master/assets/viz.pdf) which concludes:

>The number of stars of a system tends to correlate not only with the number of forks, but
also with its effective usage by other client applications, which reinforces the importance
of stars as a real measure of a system’s popularity.

In the future, other stats such as issues, pull requests, followers gained, etc could be included.

## How Are Stats for Users and Orgs Calculated?

To provide star counts for users and orgs, `Viz` groups repo stars by user or org.  Note the `stars:>=100` restriction still applies to counted repos.

## Can We See Visualizations in R or Python?

Interested in visualizations with Python or R?  [Contribute](https://www.github.com/donnemartin/viz/CONTRIBUTING)! :)

## What Languages Are Tracked?

`Viz` tracks the most popular languages on GitHub plus the `Unknown` language option.  Data from each language is tallied to determine the overall stats.

Missing a popular language below?  Feel free to file a [request](https://github.com/donnemartin/viz/issues).

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

## Is Viz Affiliated with GitHub?

No, `Viz` is not affiliated with GitHub.  `Viz` is a community project by the GitHub community, for the GitHub community.

## Can We Contribute?

Contributions are welcome!

Review the [Contributing Guidelines](https://www.github.com/donnemartin/viz/CONTRIBUTING) for details on how to:

* Submit issues
* Submit pull requests

## How Do We Contact You?

Contact details are on my [GitHub Profile](https://github.com/donnemartin).

You can also file a ticket on the [issue tracker](https://github.com/donnemartin/viz/issues).

## What is the License for Viz?

    Copyright 2016 Donne Martin

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
