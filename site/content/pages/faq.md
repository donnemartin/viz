Title: FAQ
Date: 2016-01-01 06:00

### Why Viz?

Viewing raw stats and tables only tell you **part of a story**.

![Imgur](http://i.imgur.com/bIryNpL.png)

`Viz` helps tell the rest of the story with **interactive visualizations** that are **continually updated**.

![Imgur](http://i.imgur.com/HBzXqrN.png)

### How Do We Help or Stay Up-To-Date With the Evolution of Viz?

`Viz` is just getting started.  Help spread the word!

[Contributions](https://github.com/donnemartin/viz/blob/master/CONTRIBUTING.md) and [feedback](https://github.com/donnemartin/viz/issues) are welcome.

Feel free to [follow](https://www.github.com/donnemartin), [star](https://github.com/donnemartin/viz), [fork](https://github.com/donnemartin/viz/fork), and check back for updates.

<iframe src="https://ghbtns.com/github-btn.html?user=donnemartin&type=follow&count=true" frameborder="0" scrolling="0" width="145" height="20"></iframe>
<iframe id="gh-star" src="https://ghbtns.com/github-btn.html?user=donnemartin&amp;repo=viz&amp;type=star&amp;count=false" allowtransparency="true" frameborder="0" scrolling="0" width="50" height="20"></iframe>
<iframe id="gh-fork" src="https://ghbtns.com/github-btn.html?user=donnemartin&amp;repo=viz&amp;type=fork" allowtransparency="true" frameborder="0" scrolling="0" width="53" height="20"></iframe>

### How Do We Navigate Viz?

Each dashboard within `Viz` offers different levels of interactivity.  Try:

* Interacting with the filters.
* Hovering over elements to view tooltip info.
* Clicking elements to highlight or filter.

You can change the activate dashboard through the following control:

<p align="center">
  <img src="http://i.imgur.com/AoCuhEF.png">
</p>

<a name="can-i-viz-offline"></a>
### Can We Viz Offline?

Yes, you'll need the **free** [Reader](http://www.tableau.com/products/reader).  Download and run the latest [Viz Workbook](https://github.com/donnemartin/viz/tree/master/viz).  This allows you to interact with a **local copy**--you'll need to download the latest workbook as updates are continually pushed.

Depending on your setup, you'll likely see **improved performance running `Viz` locally.**

### Why Does the Online Viz Reset After Several Minutes of Inactivity?

Sessions timeout after some inactivity.  For more details, [view this post](https://community.tableau.com/thread/170831) from the Tableau Forums.

### Why Isn't the Online Interactive Viz Loading for Me?

The visualization hosting service might be having issues.  Check the [status](https://trust.tableau.com/status/tableau-public).

You can also run `Viz` offline.

### Can We See Visualizations in JavaScript, Python, R or ...?

Please check out the following [ticket](https://github.com/donnemartin/viz/issues/11).

Community visualizations:

* [D3/d3fc](http://colineberhardt.github.io/d3fc-github-viz/) by [ColinEberhardt](https://github.com/ColinEberhardt)
* [Contribute](https://github.com/donnemartin/viz/issues/11)

### What Data Is Tracked?

Although [GitHub Trending](https://github.com/trending) is a **great tool to discover up-and-coming projects**, it only allows you to review up to **one month** of data.  Third-party sites often show **all-time stats** that are **relatively static**, as they are dominated by well-established repos.

`Viz` is meant to supplement existing solutions by **filtering only on the newest, most popular repos** created within a specific timeframe.

***For example, `Viz` 2017 will only track repos created within the year 2017.***

### Can We See Stats for Time Ranges Other Than 2017?

`Viz` currently provides stats for 2017, 2016, 2015, and rolling 1-, 3-, and 6-months.

### Can We See Stats for 'Older' Repos?

In the future, `Viz` can be extended to track repos regardless of creation date.  Feedback on this [ticket](https://github.com/donnemartin/viz/issues/9) is welcome.

### How Do You Mine Data?

![Imgur](http://i.imgur.com/W5hfGVo.png)

Mining data directly from GitHub, `Viz` is powered by the [GitHub API](https://developer.github.com/v3/) and leverages the following:

* [`github3.py`](https://github.com/sigmavirus24/github3.py) to access the GitHub API through Python.
* [`pandas`](https://github.com/pydata/pandas) in the following [IPython Notebook](https://github.com/donnemartin/viz/blob/master/githubstats/data_wrangling.ipynb) for data wrangling.
* [Google Maps API](https://developers.google.com/maps/?hl=en) through [`geocoder`](https://github.com/DenisCarriere/geocoder) for location data.
* [Tableau Public](https://public.tableau.com/s/) for visualizations.*

In the future, [Google BigQuery](https://cloud.google.com/bigquery/) along with [GitHub Archive](https://www.githubarchive.org/) could also supplement the GitHub API.

**Interested in visualizations with JavaScript, Python, R, or ...?  Check out the following [ticket](https://github.com/donnemartin/viz/issues/11).*

### Where Do We Find the Data?

* [Data](https://github.com/donnemartin/viz/tree/master/githubstats/data)
* [Data Tables](https://github.com/donnemartin/viz/tree/master/language_stats)
* [Tableau Workbooks](https://github.com/donnemartin/viz/tree/master/viz)

### When Did You Mine the 2017 Data?

The `Viz` 2017 stats were mined on `January 1, 2018, between 00:00 to 01:00 PDT` and include all repos created in the year 2017.  The data is preserved [here](https://github.com/donnemartin/viz/tree/master/language_stats/2017_frozen).

### Why Are My 2017 Manual Search Results Different From Viz 2017?

With [GitHub Search](https://github.com/search), you can manually run queries similar to what you would get from the GitHub API.

To view the most-starred JavaScript repos created in 2017, run the following [query](https://github.com/search?utf8=%E2%9C%93&q=created%3A2017-01-01..2017-12-31+stars%3A%3E%3D100+language%3Ajavascript&type=Repositories&ref=searchresults):

    created:2017-01-01..2017-12-31 stars:>=100 language:javascript

To check stats for a user's or an org's repos that were created in 2017, run:

    created:2017-01-01..2017-12-31 stars:>=100 user:user_name

*Star counts from the searches above will show data up to the time you performed the search.*

### Why Restrict Search Results to `stars:>=100` or `stars:>=500` for Viz 2017?

Only repos with `stars:>=100` are tracked to help filter GitHub's rapidly growing **49+ million** repositories and to keep within the [GitHub API rate limits](https://developer.github.com/v3/rate_limit/).

Some visualizations with additional data such as `pull requests`, `issues`, `contributors`, and `commits` filter repos with `stars:>=500`

`Viz` 6-, 3-, and 1-month might loosen this restriction as there should be less repos to analyze.  [Google BigQuery](https://cloud.google.com/bigquery/) along with [GitHub Archive](https://www.githubarchive.org/) could also supplement the GitHub API.

### Why Stars and Forks?

`Viz` provides stats for repos, users, and orgs by stars (and in many cases, forks).  **Stars and forks are *not* perfect metrics**, yet they are **simple and fairly effective measures of interest**.  For a more detailed discussion on measuring repo popularity, check out ["On the Popularity of GitHub Applications:
 A Preliminary Note"](https://github.com/donnemartin/viz/blob/master/assets/gh-stats.pdf) which concludes:

>The number of stars of a system tends to correlate not only with the number of forks, but
also with its effective usage by other client applications, which reinforces the importance
of stars as a real measure of a system’s popularity.

#### New Support for Additional Metrics

**Update**: Viz now includes additional data such as `pull requests`, `issues`, `contributors`, and `commits`.

### How Are Stats for Users and Orgs Calculated?

To provide stats for users and orgs, `Viz` groups stars and forks by user or org.  Note the `stars:>=100` restriction still applies.

### What Languages Are Tracked?

`Viz` tracks the most popular languages on GitHub plus the `Unknown` language option.  Repo languages are identified by [github/linguist](https://github.com/github/linguist).

Missing a popular language below?  Feel free to file a [request](https://github.com/donnemartin/viz/issues).

```
languages = [
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
    'Julia',
    'Unknown',
    'Overall',
]
```

### Is Viz Affiliated With GitHub?

No, `Viz` is not affiliated with GitHub.

`Viz` is a community project by the GitHub community, for the GitHub community.

### How Do We Contribute?

Please review the [Contributing Guidelines](https://www.github.com/donnemartin/viz/CONTRIBUTING) for details on how to:

* Submit issues
* Submit pull requests

Check out the [issue tracker](https://github.com/donnemartin/viz/issues).

### How Do We Contact You?

Feel free to contact me to discuss any issues, questions, or comments.

* Email: [donne.martin@gmail.com](mailto:donne.martin@gmail.com)
* Twitter: [@donne_martin](https://twitter.com/donne_martin)
* GitHub: [donnemartin](https://github.com/donnemartin)
* LinkedIn: [donnemartin](https://www.linkedin.com/in/donnemartin)
* Website: [donnemartin.com](http://donnemartin.com)

You can also file a ticket on the [issue tracker](https://github.com/donnemartin/viz/issues).

### What Is the License for Viz?

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
