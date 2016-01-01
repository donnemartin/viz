<p align="center">
  <img src="http://www.clker.com/cliparts/v/P/n/K/B/P/stars-md.png">
</p>

# gh-stats

> The **most-starred** GitHub projects **created in** 2015, the past six months, or the past three months.  Also provides misc stats plus the most-starred users and orgs, grouped by Language and Overall.

`gh-stats` is a community project and is not affiliated with GitHub.

## Motivation

>Have you ever wondered what were the most-starred repos created in 2015?  How about the past three or six months?  Did Amazon, Apple, Facebook, Google, or Microsoft have the 'trendiest' repos?  How about individual contributors?

Although [GitHub Trending](https://github.com/trending) is a **great way to discover up-and-coming projects**, it only allows you to look at **up to one month** of data.  Third-party sites often show **all-time stats that are relatively static**, as they are dominated by well-established repos.

**`gh-stats` filters only on the latest repos created within a specific timeframe.**

*`gh-stats` provides stats for repos, developers, and orgs by stars.  Stars are by no means a perfect metric, yet they are a simple and fairly effective measure of interest.*

#### `gh-stats 2015`:

* **Only tracks repos created within 2015**.
* Provides stats for the entire 2015 year.*

**Data mined on January 1, 2016 between 00:00 to 01:00 PDT.*

#### `gh-stats Six Months`, `Three Months`:

* **Only tracks repos created within the past six months or three months**.
* Updated regularly.
* *Coming soon.*

#### `gh-stats` is also:

* Hosted on GitHub, no need to visit a third-party site.
* Open source, [contributions](https://github.com/donnemartin/gh-stats/blob/master/CONTRIBUTING.md) are welcome.
* Under active development, providing more stats in the future.  [Feedback](https://github.com/donnemartin/gh-stats/issues) is  welcome.

## Method

`gh-stats` is powered by the [GitHub API](https://developer.github.com/v3/).  You can verify the results through [GitHub Search](https://github.com/search).  For example, to view the [Most Starred Javascript Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/javascript.md#most-starred-repos-javascript) you can run the following query on [GitHub Search](https://github.com/search?utf8=%E2%9C%93&q=created%3A%3E%3D2015-01-01+stars%3A%3E%3D100+language%3Ajavascript&ref=simplesearch):

    created:>=2015-01-01 stars:>=100 language:javascript

To check stats for a user or org, run:

    created:>=2015-01-01 stars:>=100 user:user_name

**Note**: Only repos with **`stars:>=100`** are tracked to help filter GitHub's rapidly growing **30+ million** repositories and to keep within the [GitHub API rate limits](https://developer.github.com/v3/rate_limit/).

>`gh-stats` provides stats for repos, developers, and orgs by stars.  Stars are by no means a perfect metric, yet they are a simple and fairly effective measure of interest.
>
>`gh-stats` only tracks repos created within the specified timeframe.  For example, `gh-stats 2015` will only track repos created within the year 2015.

### Stats for Users and Orgs

To provide star counts for users and orgs, `gh-stats` simply groups repo stars by user or org.  Note the `stars:>=100` restriction still applies to repos counted towards users and orgs.

### Languages

Grouping is based on repo language as identified by [github/linguist](https://github.com/github/linguist).

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

The **50 overall most-starred** repos, users, and orgs:

* [Repos](https://github.com/donnemartin/gh-stats#most-starred-repos-overall)
* [Users](https://github.com/donnemartin/gh-stats#most-starred-users-overall)
* [Orgs](https://github.com/donnemartin/gh-stats#most-starred-orgs-overall)

Check out the [Language Index](#language-index) to view:

* Up to the 500 most-starred repos, users, and orgs, overall.
* Up to the 500 most-starred repos, users, and orgs, organized by language.

## Most-Starred Repos: Overall

| | Repo | Stars |
|---|---|---|
| 1. | [apple/swift](https://github.com/apple/swift) <br/>The Swift Programming Language | 24882 |
| 2. | [facebook/react-native](https://github.com/facebook/react-native) <br/>A framework for building native apps with React. | 24778 |
| 3. | [jlevy/the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line) <br/>Master the command line, in one page | 21492 |
| 4. | [NARKOZ/hacker-scripts](https://github.com/NARKOZ/hacker-scripts) <br/>Based on a true story | 19836 |
| 5. | [google/material-design-lite](https://github.com/google/material-design-lite) <br/>Material Design Lite Components in HTML/CSS/JS | 17165 |
| 6. | [nvbn/thefuck](https://github.com/nvbn/thefuck) <br/>Magnificent app which corrects your previous conso... | 16449 |
| 7. | [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) <br/> Open source software library for numerical comput... | 15544 |
| 8. | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) <br/>A list of SaaS, PaaS and IaaS offerings that have... | 12450 |
| 9. | [rackt/redux](https://github.com/rackt/redux) <br/>Predictable state container for JavaScript apps | 11610 |
| 10. | [bevacqua/dragula](https://github.com/bevacqua/dragula) <br/>:ok_hand: Drag and drop so simple it hurts | 10735 |
| 11. | [zenorocha/clipboard.js](https://github.com/zenorocha/clipboard.js) <br/>:scissors: Modern copy to clipboard. No Flash. Jus... | 10268 |
| 12. | [0xAX/linux-insides](https://github.com/0xAX/linux-insides) <br/>A little bit about a linux kernel | 10038 |
| 13. | [minimaxir/big-list-of-naughty-strings](https://github.com/minimaxir/big-list-of-naughty-strings) <br/>The Big List of Naughty Strings is a list of strin... | 9385 |
| 14. | [phanan/htaccess](https://github.com/phanan/htaccess) <br/>A collection of useful .htaccess snippets. | 8963 |
| 15. | [isocpp/CppCoreGuidelines](https://github.com/isocpp/CppCoreGuidelines) <br/>The C++ Core Guidelines are a set of tried-and-tru... | 8782 |
| 16. | [MaximAbramchuck/awesome-interviews](https://github.com/MaximAbramchuck/awesome-interviews) <br/>:octocat: A curated awesome list of lists of inter... | 8266 |
| 17. | [google/deepdream](https://github.com/google/deepdream)  | 8047 |
| 18. | [Flipboard/react-canvas](https://github.com/Flipboard/react-canvas) <br/>High performance canvas rendering for React comp... | 7410 |
| 19. | [facebook/fresco](https://github.com/facebook/fresco) <br/>An Android library for managing images and the mem... | 7385 |
| 20. | [chrissimpkins/Hack](https://github.com/chrissimpkins/Hack) <br/>A typeface designed for source code | 7204 |
| 21. | [yaronn/blessed-contrib](https://github.com/yaronn/blessed-contrib) <br/>Build terminal dashboards using ascii/ansi art and... | 7190 |
| 22. | [kilimchoi/engineering-blogs](https://github.com/kilimchoi/engineering-blogs) <br/>A curated list of engineering blogs | 7187 |
| 23. | [MostlyAdequate/mostly-adequate-guide](https://github.com/MostlyAdequate/mostly-adequate-guide) <br/>Mostly adequate guide to FP (in javascript) | 7170 |
| 24. | [cjwirth/awesome-ios-ui](https://github.com/cjwirth/awesome-ios-ui) <br/>A curated list of awesome iOS UI/UX libraries | 7027 |
| 25. | [square/leakcanary](https://github.com/square/leakcanary) <br/>A memory leak detection library for Android and Ja... | 6794 |
| 26. | [danielgindi/ios-charts](https://github.com/danielgindi/ios-charts) <br/>An iOS port of the beautiful MPAndroidChart. - Bea... | 6748 |
| 27. | [herrbischoff/awesome-osx-command-line](https://github.com/herrbischoff/awesome-osx-command-line) <br/>Use your OS X terminal shell to do awesome things. | 6492 |
| 28. | [arasatasaygin/is.js](https://github.com/arasatasaygin/is.js) <br/>Micro check library | 6466 |
| 29. | [Automattic/wp-calypso](https://github.com/Automattic/wp-calypso) <br/>The new JavaScript- and API-powered WordPress.com | 6451 |
| 30. | [HannahMitt/HomeMirror](https://github.com/HannahMitt/HomeMirror) <br/>Android application powering the mirror in my hous... | 6274 |
| 31. | [mattermost/platform](https://github.com/mattermost/platform) <br/>Open source Slack-alternative in Golang and React... | 6136 |
| 32. | [yudai/gotty](https://github.com/yudai/gotty) <br/>Share your terminal as a web application | 6003 |
| 33. | [serverless/serverless](https://github.com/serverless/serverless) <br/>Serverless (formerly JAWS): The serverless applica... | 5909 |
| 34. | [bendc/frontend-guidelines](https://github.com/bendc/frontend-guidelines) <br/>Some HTML, CSS and JS best practices. | 5776 |
| 35. | [purifycss/purifycss](https://github.com/purifycss/purifycss) <br/>Remove unused CSS. Also works with single-page app... | 5728 |
| 36. | [dotnet/coreclr](https://github.com/dotnet/coreclr) <br/>This repo contains the .NET Core runtime, called C... | 5610 |
| 37. | [ConnorAtherton/loaders.css](https://github.com/ConnorAtherton/loaders.css) <br/>Delightful, performance-focused pure css loading a... | 5573 |
| 38. | [google/fonts](https://github.com/google/fonts) <br/>Font files available from Google Fonts | 5512 |
| 39. | [facebook/relay](https://github.com/facebook/relay) <br/>Relay is a JavaScript framework for building data-... | 5323 |
| 40. | [AllThingsSmitty/css-protips](https://github.com/AllThingsSmitty/css-protips) <br/>A collection of tips to help take your CSS skills... | 5323 |
| 41. | [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat) <br/>Have your own Slack like online chat, built with M... | 5227 |
| 42. | [ampproject/amphtml](https://github.com/ampproject/amphtml) <br/>AMP HTML source code, samples, and documentation... | 5188 |
| 43. | [oneuijs/You-Dont-Need-jQuery](https://github.com/oneuijs/You-Dont-Need-jQuery) <br/>Examples of how to do query, style, dom, ajax, eve... | 5147 |
| 44. | [Netflix/falcor](https://github.com/Netflix/falcor) <br/>A JavaScript library for efficient data fetching | 5140 |
| 45. | [hacksalot/HackMyResume](https://github.com/hacksalot/HackMyResume) <br/>Generate polished résumés and CVs in HTML, Markdow... | 5090 |
| 46. | [nagadomi/waifu2x](https://github.com/nagadomi/waifu2x) <br/>Image Super-Resolution for Anime-Style Art | 5054 |
| 47. | [Mango/slideout](https://github.com/Mango/slideout) <br/>A touch slideout navigation menu for your mobile w... | 5052 |
| 48. | [neutraltone/awesome-stock-resources](https://github.com/neutraltone/awesome-stock-resources) <br/>A collection of links for free stock photography,... | 4979 |
| 49. | [equinusocio/material-theme](https://github.com/equinusocio/material-theme) <br/>Material Theme, the most epic theme for Sublime Te... | 4977 |
| 50. | [WebAssembly/design](https://github.com/WebAssembly/design) <br/>WebAssembly Design Documents | 4968 |

## Most-Starred Users: Overall

| | User | Repos | Stars |
|---|---|---|---|
| 1. | [jlevy](https://github.com/jlevy)  | [the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line)  (21492) <br/>[og-equity-compensation](https://github.com/jlevy/og-equity-compensation)  (376) <br/> | 21868 |
| 2. | [NARKOZ](https://github.com/NARKOZ)  | [hacker-scripts](https://github.com/NARKOZ/hacker-scripts)  (19836) <br/>[guides](https://github.com/NARKOZ/guides)  (1040) <br/> | 20876 |
| 3. | [bevacqua](https://github.com/bevacqua)  | [dragula](https://github.com/bevacqua/dragula)  (10735) <br/>[es6](https://github.com/bevacqua/es6)  (3143) <br/>[fuzzysearch](https://github.com/bevacqua/fuzzysearch)  (1647) <br/>[woofmark](https://github.com/bevacqua/woofmark)  (1224) <br/>[promisees](https://github.com/bevacqua/promisees)  (804) <br/>[horsey](https://github.com/bevacqua/horsey)  (667) <br/>[insignia](https://github.com/bevacqua/insignia)  (572) <br/>[perfschool](https://github.com/bevacqua/perfschool)  (411) <br/>[hit-that](https://github.com/bevacqua/hit-that)  (271) <br/>[local-storage](https://github.com/bevacqua/local-storage)  (255) <br/>[angular-dragula](https://github.com/bevacqua/angular-dragula)  (252) <br/>[react-dragula](https://github.com/bevacqua/react-dragula)  (166) <br/>[swivel](https://github.com/bevacqua/swivel)  (132) <br/>[insane](https://github.com/bevacqua/insane)  (123) <br/> | 20402 |
| 4. | [nvbn](https://github.com/nvbn)  | [thefuck](https://github.com/nvbn/thefuck)  (16449) <br/> | 16449 |
| 5. | [phanan](https://github.com/phanan)  | [htaccess](https://github.com/phanan/htaccess)  (8963) <br/>[koel](https://github.com/phanan/koel)  (4926) <br/> | 13889 |
| 6. | [ripienaar](https://github.com/ripienaar)  | [free-for-dev](https://github.com/ripienaar/free-for-dev)  (12450) <br/> | 12450 |
| 7. | [donnemartin](https://github.com/donnemartin)  | [data-science-ipython-notebooks](https://github.com/donnemartin/data-science-ipython-notebooks)  (3938) <br/>[saws](https://github.com/donnemartin/saws)  (2590) <br/>[interactive-coding-challenges](https://github.com/donnemartin/interactive-coding-challenges)  (2121) <br/>[awesome-aws](https://github.com/donnemartin/awesome-aws)  (1631) <br/>[dev-setup](https://github.com/donnemartin/dev-setup)  (1580) <br/> | 11860 |
| 8. | [sindresorhus](https://github.com/sindresorhus)  | [awesome-electron](https://github.com/sindresorhus/awesome-electron)  (4041) <br/>[speed-test](https://github.com/sindresorhus/speed-test)  (1369) <br/>[awesome-scifi](https://github.com/sindresorhus/awesome-scifi)  (894) <br/>[xo](https://github.com/sindresorhus/xo)  (820) <br/>[caprine](https://github.com/sindresorhus/caprine)  (586) <br/>[amas](https://github.com/sindresorhus/amas)  (405) <br/>[hasha](https://github.com/sindresorhus/hasha)  (399) <br/>[ama](https://github.com/sindresorhus/ama)  (380) <br/>[wallpaper](https://github.com/sindresorhus/wallpaper)  (276) <br/>[generator-electron](https://github.com/sindresorhus/generator-electron)  (250) <br/>[generator-nm](https://github.com/sindresorhus/generator-nm)  (248) <br/>[electron-boilerplate](https://github.com/sindresorhus/electron-boilerplate)  (224) <br/>[node-module-boilerplate](https://github.com/sindresorhus/node-module-boilerplate)  (220) <br/>[pageres-cli](https://github.com/sindresorhus/pageres-cli)  (202) <br/>[elegant-spinner](https://github.com/sindresorhus/elegant-spinner)  (156) <br/>[is-progressive](https://github.com/sindresorhus/is-progressive)  (146) <br/>[kill-tabs](https://github.com/sindresorhus/kill-tabs)  (145) <br/>[log-update](https://github.com/sindresorhus/log-update)  (142) <br/>[module-requests](https://github.com/sindresorhus/module-requests)  (124) <br/>[electron-debug](https://github.com/sindresorhus/electron-debug)  (117) <br/>[np](https://github.com/sindresorhus/np)  (111) <br/>[pify](https://github.com/sindresorhus/pify)  (109) <br/> | 11364 |
| 9. | [zenorocha](https://github.com/zenorocha)  | [clipboard.js](https://github.com/zenorocha/clipboard.js)  (10268) <br/> | 10268 |
| 10. | [0xAX](https://github.com/0xAX)  | [linux-insides](https://github.com/0xAX/linux-insides)  (10038) <br/> | 10038 |
| 11. | [chrissimpkins](https://github.com/chrissimpkins)  | [Hack](https://github.com/chrissimpkins/Hack)  (7204) <br/>[codeface](https://github.com/chrissimpkins/codeface)  (2807) <br/> | 10011 |
| 12. | [minimaxir](https://github.com/minimaxir)  | [big-list-of-naughty-strings](https://github.com/minimaxir/big-list-of-naughty-strings)  (9385) <br/>[copy-syntax-highlight-osx](https://github.com/minimaxir/copy-syntax-highlight-osx)  (312) <br/>[video-to-gif-osx](https://github.com/minimaxir/video-to-gif-osx)  (191) <br/> | 9888 |
| 13. | [yaronn](https://github.com/yaronn)  | [blessed-contrib](https://github.com/yaronn/blessed-contrib)  (7190) <br/>[wopr](https://github.com/yaronn/wopr)  (2042) <br/> | 9232 |
| 14. | [AllThingsSmitty](https://github.com/AllThingsSmitty)  | [css-protips](https://github.com/AllThingsSmitty/css-protips)  (5323) <br/>[jquery-tips-everyone-should-know](https://github.com/AllThingsSmitty/jquery-tips-everyone-should-know)  (3512) <br/> | 8835 |
| 15. | [ChenYilong](https://github.com/ChenYilong)  | [iOS9AdaptationTips](https://github.com/ChenYilong/iOS9AdaptationTips)  (3207) <br/>[iOSInterviewQuestions](https://github.com/ChenYilong/iOSInterviewQuestions)  (2183) <br/>[CYLTabBarController](https://github.com/ChenYilong/CYLTabBarController)  (1287) <br/>[ParseSourceCodeStudy](https://github.com/ChenYilong/ParseSourceCodeStudy)  (1038) <br/>[CollectionViewClassifyMenu](https://github.com/ChenYilong/CollectionViewClassifyMenu)  (649) <br/>[CYLTableViewPlaceHolder](https://github.com/ChenYilong/CYLTableViewPlaceHolder)  (240) <br/> | 8604 |
| 16. | [florent37](https://github.com/florent37)  | [MaterialViewPager](https://github.com/florent37/MaterialViewPager)  (3824) <br/>[HollyViewPager](https://github.com/florent37/HollyViewPager)  (649) <br/>[GlidePalette](https://github.com/florent37/GlidePalette)  (526) <br/>[MaterialLeanBack](https://github.com/florent37/MaterialLeanBack)  (483) <br/>[ViewAnimator](https://github.com/florent37/ViewAnimator)  (470) <br/>[MaterialTextField](https://github.com/florent37/MaterialTextField)  (438) <br/>[Carpaccio](https://github.com/florent37/Carpaccio)  (386) <br/>[MaterialImageLoading](https://github.com/florent37/MaterialImageLoading)  (296) <br/>[WearMenu](https://github.com/florent37/WearMenu)  (274) <br/>[BeautifulParallax](https://github.com/florent37/BeautifulParallax)  (263) <br/>[PicassoPalette](https://github.com/florent37/PicassoPalette)  (248) <br/>[OCiney-iOS](https://github.com/florent37/OCiney-iOS)  (213) <br/>[DaVinci](https://github.com/florent37/DaVinci)  (209) <br/> | 8279 |
| 17. | [MaximAbramchuck](https://github.com/MaximAbramchuck)  | [awesome-interviews](https://github.com/MaximAbramchuck/awesome-interviews)  (8266) <br/> | 8266 |
| 18. | [ibireme](https://github.com/ibireme)  | [YYText](https://github.com/ibireme/YYText)  (3882) <br/>[YYWebImage](https://github.com/ibireme/YYWebImage)  (1726) <br/>[YYModel](https://github.com/ibireme/YYModel)  (1042) <br/>[YYCache](https://github.com/ibireme/YYCache)  (531) <br/>[YYImage](https://github.com/ibireme/YYImage)  (375) <br/>[YYCategories](https://github.com/ibireme/YYCategories)  (300) <br/>[YYAsyncLayer](https://github.com/ibireme/YYAsyncLayer)  (134) <br/>[YYDispatchQueuePool](https://github.com/ibireme/YYDispatchQueuePool)  (131) <br/>[YYKeyboardManager](https://github.com/ibireme/YYKeyboardManager)  (131) <br/> | 8252 |
| 19. | [hongyangAndroid](https://github.com/hongyangAndroid)  | [AndroidAutoLayout](https://github.com/hongyangAndroid/AndroidAutoLayout)  (1557) <br/>[okhttp-utils](https://github.com/hongyangAndroid/okhttp-utils)  (920) <br/>[Highlight](https://github.com/hongyangAndroid/Highlight)  (799) <br/>[android-percent-support-extend](https://github.com/hongyangAndroid/android-percent-support-extend)  (693) <br/>[AndroidChangeSkin](https://github.com/hongyangAndroid/AndroidChangeSkin)  (660) <br/>[FlowLayout](https://github.com/hongyangAndroid/FlowLayout)  (631) <br/>[ChangeSkin](https://github.com/hongyangAndroid/ChangeSkin)  (506) <br/>[Android-CircleMenu](https://github.com/hongyangAndroid/Android-CircleMenu)  (483) <br/>[Android-StickyNavLayout](https://github.com/hongyangAndroid/Android-StickyNavLayout)  (412) <br/>[MixtureTextView](https://github.com/hongyangAndroid/MixtureTextView)  (331) <br/>[Android_Blog_Demos](https://github.com/hongyangAndroid/Android_Blog_Demos)  (324) <br/>[Android-ProgressBarWidthNumber](https://github.com/hongyangAndroid/Android-ProgressBarWidthNumber)  (236) <br/>[ColorTrackView](https://github.com/hongyangAndroid/ColorTrackView)  (215) <br/>[ColorfulStatusBar](https://github.com/hongyangAndroid/ColorfulStatusBar)  (178) <br/>[base-adapter](https://github.com/hongyangAndroid/base-adapter)  (107) <br/> | 8052 |
| 20. | [bendc](https://github.com/bendc)  | [frontend-guidelines](https://github.com/bendc/frontend-guidelines)  (5776) <br/>[animateplus](https://github.com/bendc/animateplus)  (1708) <br/>[animate](https://github.com/bendc/animate)  (369) <br/> | 7853 |
| 21. | [gaearon](https://github.com/gaearon)  | [redux-devtools](https://github.com/gaearon/redux-devtools)  (2494) <br/>[react-transform-boilerplate](https://github.com/gaearon/react-transform-boilerplate)  (2229) <br/>[redux-thunk](https://github.com/gaearon/redux-thunk)  (719) <br/>[babel-plugin-react-transform](https://github.com/gaearon/babel-plugin-react-transform)  (631) <br/>[library-boilerplate](https://github.com/gaearon/library-boilerplate)  (315) <br/>[react-pure-render](https://github.com/gaearon/react-pure-render)  (289) <br/>[react-transform-hmr](https://github.com/gaearon/react-transform-hmr)  (287) <br/>[react-side-effect](https://github.com/gaearon/react-side-effect)  (265) <br/>[react-proxy](https://github.com/gaearon/react-proxy)  (200) <br/>[react-elmish-example](https://github.com/gaearon/react-elmish-example)  (131) <br/>[react-blessed-hot-motion](https://github.com/gaearon/react-blessed-hot-motion)  (126) <br/>[dnd-core](https://github.com/gaearon/dnd-core)  (118) <br/> | 7804 |
| 22. | [cjwirth](https://github.com/cjwirth)  | [awesome-ios-ui](https://github.com/cjwirth/awesome-ios-ui)  (7027) <br/>[RichEditorView](https://github.com/cjwirth/RichEditorView)  (431) <br/> | 7458 |
| 23. | [kilimchoi](https://github.com/kilimchoi)  | [engineering-blogs](https://github.com/kilimchoi/engineering-blogs)  (7187) <br/> | 7187 |
| 24. | [tholman](https://github.com/tholman)  | [elevator.js](https://github.com/tholman/elevator.js)  (3851) <br/>[github-corners](https://github.com/tholman/github-corners)  (2376) <br/>[dom-animator](https://github.com/tholman/dom-animator)  (528) <br/>[overscroll](https://github.com/tholman/overscroll)  (238) <br/> | 6993 |
| 25. | [Aufree](https://github.com/Aufree)  | [trip-to-iOS](https://github.com/Aufree/trip-to-iOS)  (4515) <br/>[ESTMusicPlayer](https://github.com/Aufree/ESTMusicPlayer)  (1045) <br/>[phphub-ios](https://github.com/Aufree/phphub-ios)  (706) <br/>[ESTCollectionViewDropDownList](https://github.com/Aufree/ESTCollectionViewDropDownList)  (309) <br/>[Hodor](https://github.com/Aufree/Hodor)  (290) <br/> | 6865 |
| 26. | [LeaVerou](https://github.com/LeaVerou)  | [awesomplete](https://github.com/LeaVerou/awesomplete)  (4171) <br/>[bliss](https://github.com/LeaVerou/bliss)  (1407) <br/>[stretchy](https://github.com/LeaVerou/stretchy)  (939) <br/>[conic-gradient](https://github.com/LeaVerou/conic-gradient)  (249) <br/> | 6766 |
| 27. | [danielgindi](https://github.com/danielgindi)  | [ios-charts](https://github.com/danielgindi/ios-charts)  (6748) <br/> | 6748 |
| 28. | [herrbischoff](https://github.com/herrbischoff)  | [awesome-osx-command-line](https://github.com/herrbischoff/awesome-osx-command-line)  (6492) <br/> | 6492 |
| 29. | [arasatasaygin](https://github.com/arasatasaygin)  | [is.js](https://github.com/arasatasaygin/is.js)  (6466) <br/> | 6466 |
| 30. | [HannahMitt](https://github.com/HannahMitt)  | [HomeMirror](https://github.com/HannahMitt/HomeMirror)  (6274) <br/> | 6274 |
| 31. | [yudai](https://github.com/yudai)  | [gotty](https://github.com/yudai/gotty)  (6003) <br/> | 6003 |
| 32. | [ipselon](https://github.com/ipselon)  | [react-ui-builder](https://github.com/ipselon/react-ui-builder)  (3473) <br/>[structor](https://github.com/ipselon/structor)  (2426) <br/> | 5899 |
| 33. | [JohnCoates](https://github.com/JohnCoates)  | [Aerial](https://github.com/JohnCoates/Aerial)  (4777) <br/>[CSSketch](https://github.com/JohnCoates/CSSketch)  (1068) <br/> | 5845 |
| 34. | [callmecavs](https://github.com/callmecavs)  | [layzr.js](https://github.com/callmecavs/layzr.js)  (4079) <br/>[jump.js](https://github.com/callmecavs/jump.js)  (1718) <br/> | 5797 |
| 35. | [diafygi](https://github.com/diafygi)  | [webrtc-ips](https://github.com/diafygi/webrtc-ips)  (1883) <br/>[acme-tiny](https://github.com/diafygi/acme-tiny)  (1739) <br/>[letsencrypt-nosudo](https://github.com/diafygi/letsencrypt-nosudo)  (657) <br/>[gethttpsforfree](https://github.com/diafygi/gethttpsforfree)  (576) <br/>[gnu-pricing](https://github.com/diafygi/gnu-pricing)  (440) <br/>[webcrypto-examples](https://github.com/diafygi/webcrypto-examples)  (359) <br/> | 5654 |
| 36. | [NeXTs](https://github.com/NeXTs)  | [Clusterize.js](https://github.com/NeXTs/Clusterize.js)  (3991) <br/>[Jets.js](https://github.com/NeXTs/Jets.js)  (1634) <br/> | 5625 |
| 37. | [bboyfeiyu](https://github.com/bboyfeiyu)  | [android-tech-frontier](https://github.com/bboyfeiyu/android-tech-frontier)  (3674) <br/>[AndroidEventBus](https://github.com/bboyfeiyu/AndroidEventBus)  (715) <br/>[iOS-tech-frontier](https://github.com/bboyfeiyu/iOS-tech-frontier)  (613) <br/>[Colorful](https://github.com/bboyfeiyu/Colorful)  (587) <br/> | 5589 |
| 38. | [ConnorAtherton](https://github.com/ConnorAtherton)  | [loaders.css](https://github.com/ConnorAtherton/loaders.css)  (5573) <br/> | 5573 |
| 39. | [onevcat](https://github.com/onevcat)  | [Kingfisher](https://github.com/onevcat/Kingfisher)  (3245) <br/>[VVBlurPresentation](https://github.com/onevcat/VVBlurPresentation)  (752) <br/>[APNGKit](https://github.com/onevcat/APNGKit)  (724) <br/>[Rainbow](https://github.com/onevcat/Rainbow)  (410) <br/>[RandomColorSwift](https://github.com/onevcat/RandomColorSwift)  (290) <br/> | 5421 |
| 40. | [KittenYang](https://github.com/KittenYang)  | [KYGooeyMenu](https://github.com/KittenYang/KYGooeyMenu)  (1188) <br/>[KYAnimatedPageControl](https://github.com/KittenYang/KYAnimatedPageControl)  (800) <br/>[KYCuteView](https://github.com/KittenYang/KYCuteView)  (639) <br/>[A-GUIDE-TO-iOS-ANIMATION](https://github.com/KittenYang/A-GUIDE-TO-iOS-ANIMATION)  (514) <br/>[Animations](https://github.com/KittenYang/Animations)  (445) <br/>[KYJellyPullToRefresh](https://github.com/KittenYang/KYJellyPullToRefresh)  (393) <br/>[GooeyTabbar](https://github.com/KittenYang/GooeyTabbar)  (359) <br/>[KYElegantPhotoGallery](https://github.com/KittenYang/KYElegantPhotoGallery)  (347) <br/>[KYWaterWaveView](https://github.com/KittenYang/KYWaterWaveView)  (276) <br/>[KYTilePhotoLayout](https://github.com/KittenYang/KYTilePhotoLayout)  (176) <br/>[KYAsyncLoadBubble](https://github.com/KittenYang/KYAsyncLoadBubble)  (109) <br/> | 5246 |
| 41. | [hacksalot](https://github.com/hacksalot)  | [HackMyResume](https://github.com/hacksalot/HackMyResume)  (5090) <br/> | 5090 |
| 42. | [nagadomi](https://github.com/nagadomi)  | [waifu2x](https://github.com/nagadomi/waifu2x)  (5054) <br/> | 5054 |
| 43. | [auchenberg](https://github.com/auchenberg)  | [volkswagen](https://github.com/auchenberg/volkswagen)  (4716) <br/>[devtools-remote](https://github.com/auchenberg/devtools-remote)  (272) <br/> | 4988 |
| 44. | [neutraltone](https://github.com/neutraltone)  | [awesome-stock-resources](https://github.com/neutraltone/awesome-stock-resources)  (4979) <br/> | 4979 |
| 45. | [equinusocio](https://github.com/equinusocio)  | [material-theme](https://github.com/equinusocio/material-theme)  (4977) <br/> | 4977 |
| 46. | [maxogden](https://github.com/maxogden)  | [menubar](https://github.com/maxogden/menubar)  (1966) <br/>[electron-packager](https://github.com/maxogden/electron-packager)  (1005) <br/>[monu](https://github.com/maxogden/monu)  (819) <br/>[linux](https://github.com/maxogden/linux)  (446) <br/>[maintenance-modules](https://github.com/maxogden/maintenance-modules)  (221) <br/>[mississippi](https://github.com/maxogden/mississippi)  (191) <br/>[standard-format](https://github.com/maxogden/standard-format)  (135) <br/>[node-repl](https://github.com/maxogden/node-repl)  (102) <br/> | 4885 |
| 47. | [wasabeef](https://github.com/wasabeef)  | [richeditor-android](https://github.com/wasabeef/richeditor-android)  (1407) <br/>[Blurry](https://github.com/wasabeef/Blurry)  (1363) <br/>[glide-transformations](https://github.com/wasabeef/glide-transformations)  (780) <br/>[picasso-transformations](https://github.com/wasabeef/picasso-transformations)  (471) <br/>[fresco-processors](https://github.com/wasabeef/fresco-processors)  (399) <br/>[Takt](https://github.com/wasabeef/Takt)  (171) <br/>[awesome-android-tools](https://github.com/wasabeef/awesome-android-tools)  (134) <br/> | 4725 |
| 48. | [mortenjust](https://github.com/mortenjust)  | [androidtool-mac](https://github.com/mortenjust/androidtool-mac)  (3364) <br/>[droptogif](https://github.com/mortenjust/droptogif)  (1268) <br/> | 4632 |
| 49. | [lukasz-madon](https://github.com/lukasz-madon)  | [awesome-remote-job](https://github.com/lukasz-madon/awesome-remote-job)  (4624) <br/> | 4624 |
| 50. | [erikras](https://github.com/erikras)  | [react-redux-universal-hot-example](https://github.com/erikras/react-redux-universal-hot-example)  (3085) <br/>[redux-form](https://github.com/erikras/redux-form)  (1098) <br/>[ducks-modular-redux](https://github.com/erikras/ducks-modular-redux)  (424) <br/> | 4607 |

## Most-Starred Orgs: Overall

| | Org | Repos | Stars |
|---|---|---|---|
| 1. | [google](https://github.com/google)  | [material-design-lite](https://github.com/google/material-design-lite)  (17165) <br/>[deepdream](https://github.com/google/deepdream)  (8047) <br/>[fonts](https://github.com/google/fonts)  (5512) <br/>[gxui](https://github.com/google/gxui)  (3432) <br/>[yapf](https://github.com/google/yapf)  (2926) <br/>[git-appraise](https://github.com/google/git-appraise)  (2761) <br/>[gson](https://github.com/google/gson)  (2697) <br/>[styleguide](https://github.com/google/styleguide)  (2543) <br/>[roboto](https://github.com/google/roboto)  (2110) <br/>[incremental-dom](https://github.com/google/incremental-dom)  (1723) <br/>[eddystone](https://github.com/google/eddystone)  (1562) <br/>[binnavi](https://github.com/google/binnavi)  (1422) <br/>[skflow](https://github.com/google/skflow)  (1386) <br/>[googletest](https://github.com/google/googletest)  (1133) <br/>[code-prettify](https://github.com/google/code-prettify)  (931) <br/>[enjarify](https://github.com/google/enjarify)  (931) <br/>[android-classyshark](https://github.com/google/android-classyshark)  (904) <br/>[or-tools](https://github.com/google/or-tools)  (884) <br/>[mr4c](https://github.com/google/mr4c)  (760) <br/>[santa-tracker-android](https://github.com/google/santa-tracker-android)  (644) <br/>[zopfli](https://github.com/google/zopfli)  (524) <br/>[glog](https://github.com/google/glog)  (517) <br/>[inception](https://github.com/google/inception)  (507) <br/>[codesearch](https://github.com/google/codesearch)  (488) <br/>[gcm](https://github.com/google/gcm)  (455) <br/>[gopacket](https://github.com/google/gopacket)  (445) <br/>[rowhammer-test](https://github.com/google/rowhammer-test)  (443) <br/>[kythe](https://github.com/google/kythe)  (419) <br/>[badwolf](https://github.com/google/badwolf)  (383) <br/>[keyczar](https://github.com/google/keyczar)  (377) <br/>[prettytensor](https://github.com/google/prettytensor)  (368) <br/>[google-http-java-client](https://github.com/google/google-http-java-client)  (334) <br/>[re2j](https://github.com/google/re2j)  (319) <br/>[snappy-start](https://github.com/google/snappy-start)  (294) <br/>[google-java-format](https://github.com/google/google-java-format)  (260) <br/>[kati](https://github.com/google/kati)  (251) <br/>[FreeBuilder](https://github.com/google/FreeBuilder)  (233) <br/>[nsjail](https://github.com/google/nsjail)  (228) <br/>[vim-codefmt](https://github.com/google/vim-codefmt)  (203) <br/>[martian](https://github.com/google/martian)  (188) <br/>[honggfuzz](https://github.com/google/honggfuzz)  (182) <br/>[caja](https://github.com/google/caja)  (180) <br/>[multibox](https://github.com/google/multibox)  (177) <br/>[eslint-config-google](https://github.com/google/eslint-config-google)  (170) <br/>[android-gradle-dsl](https://github.com/google/android-gradle-dsl)  (163) <br/>[google-toolbox-for-mac](https://github.com/google/google-toolbox-for-mac)  (153) <br/>[google-api-dotnet-client](https://github.com/google/google-api-dotnet-client)  (149) <br/>[vim-colorscheme-primary](https://github.com/google/vim-colorscheme-primary)  (147) <br/>[spatial-media](https://github.com/google/spatial-media)  (146) <br/>[UIforETW](https://github.com/google/UIforETW)  (144) <br/>[sandbox-attacksurface-analysis-tools](https://github.com/google/sandbox-attacksurface-analysis-tools)  (144) <br/>[ngx_brotli](https://github.com/google/ngx_brotli)  (142) <br/>[syzkaller](https://github.com/google/syzkaller)  (139) <br/>[mozc](https://github.com/google/mozc)  (138) <br/>[shaderc](https://github.com/google/shaderc)  (133) <br/>[google-api-java-client-samples](https://github.com/google/google-api-java-client-samples)  (132) <br/>[zooshi](https://github.com/google/zooshi)  (131) <br/>[password-alert](https://github.com/google/password-alert)  (120) <br/>[ringdroid](https://github.com/google/ringdroid)  (118) <br/>[caliper](https://github.com/google/caliper)  (117) <br/>[cups-connector](https://github.com/google/cups-connector)  (117) <br/>[flatui](https://github.com/google/flatui)  (114) <br/>[omaha](https://github.com/google/omaha)  (114) <br/>[google-api-objectivec-client](https://github.com/google/google-api-objectivec-client)  (110) <br/> | 70089 |
| 2. | [facebook](https://github.com/facebook)  | [react-native](https://github.com/facebook/react-native)  (24778) <br/>[fresco](https://github.com/facebook/fresco)  (7385) <br/>[relay](https://github.com/facebook/relay)  (5323) <br/>[stetho](https://github.com/facebook/stetho)  (3797) <br/>[nuclide](https://github.com/facebook/nuclide)  (3331) <br/>[PathPicker](https://github.com/facebook/PathPicker)  (2660) <br/>[graphql](https://github.com/facebook/graphql)  (2165) <br/>[fixed-data-table](https://github.com/facebook/fixed-data-table)  (1845) <br/>[mention-bot](https://github.com/facebook/mention-bot)  (1680) <br/>[shimmer-android](https://github.com/facebook/shimmer-android)  (1204) <br/>[network-connection-class](https://github.com/facebook/network-connection-class)  (1180) <br/>[FBSimulatorControl](https://github.com/facebook/FBSimulatorControl)  (1159) <br/>[device-year-class](https://github.com/facebook/device-year-class)  (1096) <br/>[dataloader](https://github.com/facebook/dataloader)  (574) <br/>[jscodeshift](https://github.com/facebook/jscodeshift)  (468) <br/>[screenshot-tests-for-android](https://github.com/facebook/screenshot-tests-for-android)  (384) <br/>[FBFetchedResultsController](https://github.com/facebook/FBFetchedResultsController)  (326) <br/>[fbjs](https://github.com/facebook/fbjs)  (305) <br/>[react-native-fbsdk](https://github.com/facebook/react-native-fbsdk)  (239) <br/>[Stack-RNN](https://github.com/facebook/Stack-RNN)  (228) <br/>[eyescream](https://github.com/facebook/eyescream)  (216) <br/>[WebDriverAgent](https://github.com/facebook/WebDriverAgent)  (206) <br/>[fboss](https://github.com/facebook/fboss)  (175) <br/>[bAbI-tasks](https://github.com/facebook/bAbI-tasks)  (160) <br/>[ThreatExchange](https://github.com/facebook/ThreatExchange)  (140) <br/>[react-native-applinks](https://github.com/facebook/react-native-applinks)  (117) <br/>[openbmc](https://github.com/facebook/openbmc)  (108) <br/> | 61249 |
| 3. | [apple](https://github.com/apple)  | [swift](https://github.com/apple/swift)  (24882) <br/>[swift-package-manager](https://github.com/apple/swift-package-manager)  (3131) <br/>[swift-evolution](https://github.com/apple/swift-evolution)  (2250) <br/>[swift-corelibs-foundation](https://github.com/apple/swift-corelibs-foundation)  (1492) <br/>[swift-corelibs-libdispatch](https://github.com/apple/swift-corelibs-libdispatch)  (567) <br/>[swift-corelibs-xctest](https://github.com/apple/swift-corelibs-xctest)  (383) <br/>[swift-llvm](https://github.com/apple/swift-llvm)  (353) <br/>[swift-3-api-guidelines-review](https://github.com/apple/swift-3-api-guidelines-review)  (330) <br/>[swift-clang](https://github.com/apple/swift-clang)  (309) <br/>[swift-lldb](https://github.com/apple/swift-lldb)  (269) <br/>[swift-llbuild](https://github.com/apple/swift-llbuild)  (248) <br/>[example-package-dealer](https://github.com/apple/example-package-dealer)  (118) <br/>[example-package-playingcard](https://github.com/apple/example-package-playingcard)  (105) <br/>[example-package-fisheryates](https://github.com/apple/example-package-fisheryates)  (103) <br/> | 34540 |
| 4. | [Yalantis](https://github.com/Yalantis)  | [Side-Menu.Android](https://github.com/Yalantis/Side-Menu.Android)  (2468) <br/>[FoldingTabBar.iOS](https://github.com/Yalantis/FoldingTabBar.iOS)  (2145) <br/>[StarWars.iOS](https://github.com/Yalantis/StarWars.iOS)  (1987) <br/>[Phoenix](https://github.com/Yalantis/Phoenix)  (1984) <br/>[Context-Menu.Android](https://github.com/Yalantis/Context-Menu.Android)  (1930) <br/>[GuillotineMenu](https://github.com/Yalantis/GuillotineMenu)  (1768) <br/>[Persei](https://github.com/Yalantis/Persei)  (1707) <br/>[Koloda](https://github.com/Yalantis/Koloda)  (1644) <br/>[Pull-to-Refresh.Rentals-iOS](https://github.com/Yalantis/Pull-to-Refresh.Rentals-iOS)  (1639) <br/>[Side-Menu.iOS](https://github.com/Yalantis/Side-Menu.iOS)  (1559) <br/>[GuillotineMenu-Android](https://github.com/Yalantis/GuillotineMenu-Android)  (1504) <br/>[Context-Menu.iOS](https://github.com/Yalantis/Context-Menu.iOS)  (1222) <br/>[FlipViewPager.Draco](https://github.com/Yalantis/FlipViewPager.Draco)  (1220) <br/>[Euclid](https://github.com/Yalantis/Euclid)  (1201) <br/>[Taurus](https://github.com/Yalantis/Taurus)  (947) <br/>[PullToMakeSoup](https://github.com/Yalantis/PullToMakeSoup)  (930) <br/>[StarWars.Android](https://github.com/Yalantis/StarWars.Android)  (898) <br/>[Preloader.Ophiuchus](https://github.com/Yalantis/Preloader.Ophiuchus)  (675) <br/>[PullToRefresh](https://github.com/Yalantis/PullToRefresh)  (293) <br/>[PullToMakeFlight](https://github.com/Yalantis/PullToMakeFlight)  (262) <br/>[YALField](https://github.com/Yalantis/YALField)  (225) <br/>[CloudKit-Demo.Swift](https://github.com/Yalantis/CloudKit-Demo.Swift)  (117) <br/>[Watchface-Constructor](https://github.com/Yalantis/Watchface-Constructor)  (110) <br/> | 28435 |
| 5. | [Microsoft](https://github.com/Microsoft)  | [WinObjC](https://github.com/Microsoft/WinObjC)  (4842) <br/>[msbuild](https://github.com/Microsoft/msbuild)  (2415) <br/>[Windows-universal-samples](https://github.com/Microsoft/Windows-universal-samples)  (2156) <br/>[DMTK](https://github.com/Microsoft/DMTK)  (1297) <br/>[nodejs-guidelines](https://github.com/Microsoft/nodejs-guidelines)  (1197) <br/>[GSL](https://github.com/Microsoft/GSL)  (1150) <br/>[nodejstools](https://github.com/Microsoft/nodejstools)  (973) <br/>[PTVS](https://github.com/Microsoft/PTVS)  (784) <br/>[Windows-Driver-Frameworks](https://github.com/Microsoft/Windows-Driver-Frameworks)  (597) <br/>[Windows-driver-samples](https://github.com/Microsoft/Windows-driver-samples)  (528) <br/>[microsoft-pdb](https://github.com/Microsoft/microsoft-pdb)  (485) <br/>[IEDiagnosticsAdapter](https://github.com/Microsoft/IEDiagnosticsAdapter)  (476) <br/>[DirectX-Graphics-Samples](https://github.com/Microsoft/DirectX-Graphics-Samples)  (429) <br/>[rDSN](https://github.com/Microsoft/rDSN)  (426) <br/>[ngconf2015demo](https://github.com/Microsoft/ngconf2015demo)  (392) <br/>[CodeContracts](https://github.com/Microsoft/CodeContracts)  (387) <br/>[ProjectOxford-ClientSDK](https://github.com/Microsoft/ProjectOxford-ClientSDK)  (383) <br/>[DirectXTK](https://github.com/Microsoft/DirectXTK)  (373) <br/>[multiverso](https://github.com/Microsoft/multiverso)  (342) <br/>[Microsoft.IO.RecyclableMemoryStream](https://github.com/Microsoft/Microsoft.IO.RecyclableMemoryStream)  (317) <br/>[react-native-code-push](https://github.com/Microsoft/react-native-code-push)  (316) <br/>[Git-Credential-Manager-for-Windows](https://github.com/Microsoft/Git-Credential-Manager-for-Windows)  (287) <br/>[GraphView](https://github.com/Microsoft/GraphView)  (282) <br/>[automatic-graph-layout](https://github.com/Microsoft/automatic-graph-layout)  (256) <br/>[MIEngine](https://github.com/Microsoft/MIEngine)  (254) <br/>[lightlda](https://github.com/Microsoft/lightlda)  (244) <br/>[WPF-Samples](https://github.com/Microsoft/WPF-Samples)  (223) <br/>[JSanity](https://github.com/Microsoft/JSanity)  (221) <br/>[TypeScript-Handbook](https://github.com/Microsoft/TypeScript-Handbook)  (190) <br/>[vscode-docs](https://github.com/Microsoft/vscode-docs)  (173) <br/>[FFmpegInterop](https://github.com/Microsoft/FFmpegInterop)  (173) <br/>[HealthClinic.biz](https://github.com/Microsoft/HealthClinic.biz)  (164) <br/>[cordova-samples](https://github.com/Microsoft/cordova-samples)  (163) <br/>[vsminecraft](https://github.com/Microsoft/vsminecraft)  (162) <br/>[XamlBehaviors](https://github.com/Microsoft/XamlBehaviors)  (154) <br/>[PartsUnlimited](https://github.com/Microsoft/PartsUnlimited)  (151) <br/>[DirectXTex](https://github.com/Microsoft/DirectXTex)  (137) <br/>[Sora](https://github.com/Microsoft/Sora)  (133) <br/>[SparkCLR](https://github.com/Microsoft/SparkCLR)  (118) <br/>[VSSDK-Extensibility-Samples](https://github.com/Microsoft/VSSDK-Extensibility-Samples)  (115) <br/> | 23865 |
| 6. | [rackt](https://github.com/rackt)  | [redux](https://github.com/rackt/redux)  (11610) <br/>[react-redux](https://github.com/rackt/react-redux)  (1678) <br/>[redux-simple-router](https://github.com/rackt/redux-simple-router)  (1272) <br/>[reselect](https://github.com/rackt/reselect)  (1257) <br/>[history](https://github.com/rackt/history)  (828) <br/>[react-a11y](https://github.com/rackt/react-a11y)  (531) <br/>[async-props](https://github.com/rackt/async-props)  (166) <br/>[scroll-behavior](https://github.com/rackt/scroll-behavior)  (101) <br/> | 17443 |
| 7. | [tensorflow](https://github.com/tensorflow)  | [tensorflow](https://github.com/tensorflow/tensorflow)  (15544) <br/> | 15544 |
| 8. | [square](https://github.com/square)  | [leakcanary](https://github.com/square/leakcanary)  (6794) <br/>[sqlbrite](https://github.com/square/sqlbrite)  (1973) <br/>[Valet](https://github.com/square/Valet)  (1459) <br/>[keywhiz](https://github.com/square/keywhiz)  (1220) <br/>[spacecommander](https://github.com/square/spacecommander)  (500) <br/>[haha](https://github.com/square/haha)  (363) <br/>[field-kit](https://github.com/square/field-kit)  (354) <br/>[certstrap](https://github.com/square/certstrap)  (308) <br/>[duktape-android](https://github.com/square/duktape-android)  (198) <br/>[inspect](https://github.com/square/inspect)  (159) <br/>[git-fastclone](https://github.com/square/git-fastclone)  (129) <br/> | 13457 |
| 9. | [googlesamples](https://github.com/googlesamples)  | [android-UniversalMusicPlayer](https://github.com/googlesamples/android-UniversalMusicPlayer)  (4364) <br/>[android-topeka](https://github.com/googlesamples/android-topeka)  (2845) <br/>[android-testing-templates](https://github.com/googlesamples/android-testing-templates)  (1133) <br/>[android-ndk](https://github.com/googlesamples/android-ndk)  (777) <br/>[google-services](https://github.com/googlesamples/google-services)  (637) <br/>[easypermissions](https://github.com/googlesamples/easypermissions)  (531) <br/>[android-vision](https://github.com/googlesamples/android-vision)  (436) <br/>[io2015-codelabs](https://github.com/googlesamples/io2015-codelabs)  (433) <br/>[easygoogle](https://github.com/googlesamples/easygoogle)  (423) <br/>[android-RuntimePermissions](https://github.com/googlesamples/android-RuntimePermissions)  (330) <br/>[android-FingerprintDialog](https://github.com/googlesamples/android-FingerprintDialog)  (315) <br/>[android-XYZTouristAttractions](https://github.com/googlesamples/android-XYZTouristAttractions)  (222) <br/>[android-play-places](https://github.com/googlesamples/android-play-places)  (164) <br/>[android-play-games-in-motion](https://github.com/googlesamples/android-play-games-in-motion)  (142) <br/>[android-nearby](https://github.com/googlesamples/android-nearby)  (123) <br/>[tango-examples-unity](https://github.com/googlesamples/tango-examples-unity)  (102) <br/> | 12977 |
| 10. | [dotnet](https://github.com/dotnet)  | [coreclr](https://github.com/dotnet/coreclr)  (5610) <br/>[roslyn](https://github.com/dotnet/roslyn)  (4132) <br/>[llilc](https://github.com/dotnet/llilc)  (951) <br/>[wcf](https://github.com/dotnet/wcf)  (552) <br/>[codeformatter](https://github.com/dotnet/codeformatter)  (504) <br/>[cli](https://github.com/dotnet/cli)  (245) <br/>[corefxlab](https://github.com/dotnet/corefxlab)  (226) <br/>[corert](https://github.com/dotnet/corert)  (182) <br/> | 12402 |
| 11. | [yahoo](https://github.com/yahoo)  | [anthelion](https://github.com/yahoo/anthelion)  (2607) <br/>[kafka-manager](https://github.com/yahoo/kafka-manager)  (1714) <br/>[gryffin](https://github.com/yahoo/gryffin)  (1665) <br/>[mysql_perf_analyzer](https://github.com/yahoo/mysql_perf_analyzer)  (1209) <br/>[squidb](https://github.com/yahoo/squidb)  (1063) <br/>[webseclab](https://github.com/yahoo/webseclab)  (868) <br/>[redislite](https://github.com/yahoo/redislite)  (326) <br/>[xss-filters](https://github.com/yahoo/xss-filters)  (258) <br/>[egads](https://github.com/yahoo/egads)  (253) <br/>[end-to-end](https://github.com/yahoo/end-to-end)  (180) <br/>[react-i13n](https://github.com/yahoo/react-i13n)  (153) <br/>[ember-intl](https://github.com/yahoo/ember-intl)  (149) <br/>[rtrace](https://github.com/yahoo/rtrace)  (129) <br/>[react-dnd-touch-backend](https://github.com/yahoo/react-dnd-touch-backend)  (114) <br/>[fluxible-router](https://github.com/yahoo/fluxible-router)  (107) <br/> | 10795 |
| 12. | [hashicorp](https://github.com/hashicorp)  | [otto](https://github.com/hashicorp/otto)  (3947) <br/>[vault](https://github.com/hashicorp/vault)  (3862) <br/>[nomad](https://github.com/hashicorp/nomad)  (1190) <br/>[go-memdb](https://github.com/hashicorp/go-memdb)  (283) <br/>[go-getter](https://github.com/hashicorp/go-getter)  (181) <br/>[go-immutable-radix](https://github.com/hashicorp/go-immutable-radix)  (121) <br/> | 9584 |
| 13. | [Flipboard](https://github.com/Flipboard)  | [react-canvas](https://github.com/Flipboard/react-canvas)  (7410) <br/>[bottomsheet](https://github.com/Flipboard/bottomsheet)  (1594) <br/> | 9004 |
| 14. | [airbnb](https://github.com/airbnb)  | [aerosolve](https://github.com/airbnb/aerosolve)  (2623) <br/>[enzyme](https://github.com/airbnb/enzyme)  (2336) <br/>[airflow](https://github.com/airbnb/airflow)  (1611) <br/>[AirMapView](https://github.com/airbnb/AirMapView)  (1039) <br/>[DeepLinkDispatch](https://github.com/airbnb/DeepLinkDispatch)  (906) <br/>[css](https://github.com/airbnb/css)  (420) <br/> | 8935 |
| 15. | [isocpp](https://github.com/isocpp)  | [CppCoreGuidelines](https://github.com/isocpp/CppCoreGuidelines)  (8782) <br/> | 8782 |
| 16. | [Netflix](https://github.com/Netflix)  | [falcor](https://github.com/Netflix/falcor)  (5140) <br/>[vector](https://github.com/Netflix/vector)  (1603) <br/>[sleepy-puppy](https://github.com/Netflix/sleepy-puppy)  (542) <br/>[lemur](https://github.com/Netflix/lemur)  (377) <br/>[Surus](https://github.com/Netflix/Surus)  (240) <br/>[Fenzo](https://github.com/Netflix/Fenzo)  (230) <br/>[ember-nf-graph](https://github.com/Netflix/ember-nf-graph)  (197) <br/>[rend](https://github.com/Netflix/rend)  (148) <br/>[falcor-express-demo](https://github.com/Netflix/falcor-express-demo)  (104) <br/>[falcor-router-demo](https://github.com/Netflix/falcor-router-demo)  (100) <br/> | 8681 |
| 17. | [forkingdog](https://github.com/forkingdog)  | [UITableView-FDTemplateLayoutCell](https://github.com/forkingdog/UITableView-FDTemplateLayoutCell)  (4069) <br/>[FDFullscreenPopGesture](https://github.com/forkingdog/FDFullscreenPopGesture)  (1831) <br/>[FDStackView](https://github.com/forkingdog/FDStackView)  (1485) <br/>[UIView-FDCollapsibleConstraints](https://github.com/forkingdog/UIView-FDCollapsibleConstraints)  (743) <br/> | 8128 |
| 18. | [MostlyAdequate](https://github.com/MostlyAdequate)  | [mostly-adequate-guide](https://github.com/MostlyAdequate/mostly-adequate-guide)  (7170) <br/> | 7170 |
| 19. | [twitter](https://github.com/twitter)  | [labella.js](https://github.com/twitter/labella.js)  (3045) <br/>[diffy](https://github.com/twitter/diffy)  (2398) <br/>[mysos](https://github.com/twitter/mysos)  (619) <br/>[torch-autograd](https://github.com/twitter/torch-autograd)  (286) <br/>[twitter-kit-android](https://github.com/twitter/twitter-kit-android)  (222) <br/>[d3kit](https://github.com/twitter/d3kit)  (168) <br/>[digits-android](https://github.com/twitter/digits-android)  (158) <br/>[whiskey](https://github.com/twitter/whiskey)  (128) <br/> | 7024 |
| 20. | [Automattic](https://github.com/Automattic)  | [wp-calypso](https://github.com/Automattic/wp-calypso)  (6451) <br/>[amp-wp](https://github.com/Automattic/amp-wp)  (265) <br/> | 6716 |
| 21. | [docker](https://github.com/docker)  | [dockercraft](https://github.com/docker/dockercraft)  (3322) <br/>[docker-bench-security](https://github.com/docker/docker-bench-security)  (1031) <br/>[libnetwork](https://github.com/docker/libnetwork)  (553) <br/>[notary](https://github.com/docker/notary)  (460) <br/>[toolbox](https://github.com/docker/toolbox)  (435) <br/>[containerd](https://github.com/docker/containerd)  (278) <br/>[libcompose](https://github.com/docker/libcompose)  (253) <br/>[leeroy](https://github.com/docker/leeroy)  (138) <br/>[libkv](https://github.com/docker/libkv)  (131) <br/> | 6601 |
| 22. | [mattermost](https://github.com/mattermost)  | [platform](https://github.com/mattermost/platform)  (6136) <br/> | 6136 |
| 23. | [purifycss](https://github.com/purifycss)  | [purifycss](https://github.com/purifycss/purifycss)  (5728) <br/>[gulp-purifycss](https://github.com/purifycss/gulp-purifycss)  (139) <br/>[grunt-purifycss](https://github.com/purifycss/grunt-purifycss)  (125) <br/> | 5992 |
| 24. | [serverless](https://github.com/serverless)  | [serverless](https://github.com/serverless/serverless)  (5909) <br/> | 5909 |
| 25. | [WebAssembly](https://github.com/WebAssembly)  | [design](https://github.com/WebAssembly/design)  (4968) <br/>[binaryen](https://github.com/WebAssembly/binaryen)  (349) <br/>[ilwasm](https://github.com/WebAssembly/ilwasm)  (197) <br/>[v8-native-prototype](https://github.com/WebAssembly/v8-native-prototype)  (182) <br/>[polyfill-prototype-1](https://github.com/WebAssembly/polyfill-prototype-1)  (161) <br/> | 5857 |
| 26. | [FormidableLabs](https://github.com/FormidableLabs)  | [radium](https://github.com/FormidableLabs/radium)  (2490) <br/>[spectacle](https://github.com/FormidableLabs/spectacle)  (2054) <br/>[victory](https://github.com/FormidableLabs/victory)  (633) <br/>[component-playground](https://github.com/FormidableLabs/component-playground)  (286) <br/>[react-flux-concepts](https://github.com/FormidableLabs/react-flux-concepts)  (251) <br/> | 5714 |
| 27. | [IFTTT](https://github.com/IFTTT)  | [RazzleDazzle](https://github.com/IFTTT/RazzleDazzle)  (1713) <br/>[FastttCamera](https://github.com/IFTTT/FastttCamera)  (1312) <br/>[jot](https://github.com/IFTTT/jot)  (1221) <br/>[polo](https://github.com/IFTTT/polo)  (380) <br/>[dash](https://github.com/IFTTT/dash)  (253) <br/>[IFTTTLaunchImage](https://github.com/IFTTT/IFTTTLaunchImage)  (243) <br/>[kashmir](https://github.com/IFTTT/kashmir)  (212) <br/>[SparkleMotion](https://github.com/IFTTT/SparkleMotion)  (111) <br/> | 5445 |
| 28. | [thoughtbot](https://github.com/thoughtbot)  | [til](https://github.com/thoughtbot/til)  (2924) <br/>[administrate](https://github.com/thoughtbot/administrate)  (2001) <br/>[Runes](https://github.com/thoughtbot/Runes)  (332) <br/>[Curry](https://github.com/thoughtbot/Curry)  (111) <br/> | 5368 |
| 29. | [coodict](https://github.com/coodict)  | [javascript-in-one-pic](https://github.com/coodict/javascript-in-one-pic)  (4578) <br/>[python3-in-one-pic](https://github.com/coodict/python3-in-one-pic)  (686) <br/> | 5264 |
| 30. | [RocketChat](https://github.com/RocketChat)  | [Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)  (5227) <br/> | 5227 |
| 31. | [ampproject](https://github.com/ampproject)  | [amphtml](https://github.com/ampproject/amphtml)  (5188) <br/> | 5188 |
| 32. | [oneuijs](https://github.com/oneuijs)  | [You-Dont-Need-jQuery](https://github.com/oneuijs/You-Dont-Need-jQuery)  (5147) <br/> | 5147 |
| 33. | [Mango](https://github.com/Mango)  | [slideout](https://github.com/Mango/slideout)  (5052) <br/> | 5052 |
| 34. | [alibaba](https://github.com/alibaba)  | [AndFix](https://github.com/alibaba/AndFix)  (2252) <br/>[dexposed](https://github.com/alibaba/dexposed)  (2192) <br/>[f2etest](https://github.com/alibaba/f2etest)  (550) <br/> | 4994 |
| 35. | [graphql](https://github.com/graphql)  | [graphql-js](https://github.com/graphql/graphql-js)  (2818) <br/>[graphiql](https://github.com/graphql/graphiql)  (854) <br/>[express-graphql](https://github.com/graphql/express-graphql)  (492) <br/>[graphql-relay-js](https://github.com/graphql/graphql-relay-js)  (333) <br/>[libgraphqlparser](https://github.com/graphql/libgraphqlparser)  (222) <br/> | 4719 |
| 36. | [laravel](https://github.com/laravel)  | [lumen](https://github.com/laravel/lumen)  (3238) <br/>[spark](https://github.com/laravel/spark)  (1086) <br/>[lumen-framework](https://github.com/laravel/lumen-framework)  (385) <br/> | 4709 |
| 37. | [primer](https://github.com/primer)  | [primer](https://github.com/primer/primer)  (4489) <br/> | 4489 |
| 38. | [ResearchKit](https://github.com/ResearchKit)  | [ResearchKit](https://github.com/ResearchKit/ResearchKit)  (4230) <br/>[AppCore](https://github.com/ResearchKit/AppCore)  (239) <br/> | 4469 |
| 39. | [PerfectlySoft](https://github.com/PerfectlySoft)  | [Perfect](https://github.com/PerfectlySoft/Perfect)  (4436) <br/> | 4436 |
| 40. | [zulip](https://github.com/zulip)  | [zulip](https://github.com/zulip/zulip)  (3526) <br/>[zulip-ios](https://github.com/zulip/zulip-ios)  (446) <br/>[zulip-android](https://github.com/zulip/zulip-android)  (222) <br/>[zulip-desktop](https://github.com/zulip/zulip-desktop)  (209) <br/> | 4403 |
| 41. | [ParsePlatform](https://github.com/ParsePlatform)  | [Parse-SDK-iOS-OSX](https://github.com/ParsePlatform/Parse-SDK-iOS-OSX)  (1664) <br/>[Parse-SDK-Android](https://github.com/ParsePlatform/Parse-SDK-Android)  (902) <br/>[ParseReact](https://github.com/ParsePlatform/ParseReact)  (826) <br/>[AnyPhone](https://github.com/ParsePlatform/AnyPhone)  (209) <br/>[parse-cli](https://github.com/ParsePlatform/parse-cli)  (209) <br/>[Parse-SDK-JS](https://github.com/ParsePlatform/Parse-SDK-JS)  (195) <br/>[parse-embedded-sdks](https://github.com/ParsePlatform/parse-embedded-sdks)  (175) <br/>[Docs](https://github.com/ParsePlatform/Docs)  (114) <br/> | 4294 |
| 42. | [XX-net](https://github.com/XX-net)  | [XX-Net](https://github.com/XX-net/XX-Net)  (4137) <br/> | 4137 |
| 43. | [Selz](https://github.com/Selz)  | [plyr](https://github.com/Selz/plyr)  (4017) <br/> | 4017 |
| 44. | [git-up](https://github.com/git-up)  | [GitUp](https://github.com/git-up/GitUp)  (3958) <br/> | 3958 |
| 45. | [pinterest](https://github.com/pinterest)  | [PINRemoteImage](https://github.com/pinterest/PINRemoteImage)  (1999) <br/>[PINCache](https://github.com/pinterest/PINCache)  (747) <br/>[mysql_utils](https://github.com/pinterest/mysql_utils)  (530) <br/>[pinball](https://github.com/pinterest/pinball)  (484) <br/>[terrapin](https://github.com/pinterest/terrapin)  (143) <br/> | 3903 |
| 46. | [plotly](https://github.com/plotly)  | [plotly.js](https://github.com/plotly/plotly.js)  (3849) <br/> | 3849 |
| 47. | [apache](https://github.com/apache)  | [incubator-zeppelin](https://github.com/apache/incubator-zeppelin)  (1015) <br/>[groovy](https://github.com/apache/groovy)  (847) <br/>[incubator-singa](https://github.com/apache/incubator-singa)  (435) <br/>[incubator-geode](https://github.com/apache/incubator-geode)  (361) <br/>[ignite](https://github.com/apache/ignite)  (238) <br/>[kylin](https://github.com/apache/kylin)  (232) <br/>[cordova-plugin-whitelist](https://github.com/apache/cordova-plugin-whitelist)  (199) <br/>[incubator-systemml](https://github.com/apache/incubator-systemml)  (150) <br/>[samza](https://github.com/apache/samza)  (142) <br/>[incubator-tinkerpop](https://github.com/apache/incubator-tinkerpop)  (105) <br/> | 3724 |
| 48. | [tmux](https://github.com/tmux)  | [tmux](https://github.com/tmux/tmux)  (3639) <br/> | 3639 |
| 49. | [dropbox](https://github.com/dropbox)  | [hackpad](https://github.com/dropbox/hackpad)  (2485) <br/>[scooter](https://github.com/dropbox/scooter)  (438) <br/>[css-style-guide](https://github.com/dropbox/css-style-guide)  (303) <br/>[nn](https://github.com/dropbox/nn)  (173) <br/>[SwiftyDropbox](https://github.com/dropbox/SwiftyDropbox)  (157) <br/> | 3556 |
| 50. | [css-modules](https://github.com/css-modules)  | [css-modules](https://github.com/css-modules/css-modules)  (2354) <br/>[webpack-demo](https://github.com/css-modules/webpack-demo)  (540) <br/>[css-modulesify](https://github.com/css-modules/css-modulesify)  (246) <br/>[icss](https://github.com/css-modules/icss)  (210) <br/>[postcss-modules-local-by-default](https://github.com/css-modules/postcss-modules-local-by-default)  (195) <br/> | 3545 |

## Language Index


View up to the 500 most-starred repos, users, and orgs, organized by language.

Because of the large number of languages tracked and the lengthy lists for each language, stats for each language can be found in [gh-stats/language_stats/2015/](https://github.com/donnemartin/gh-stats/tree/master/language_stats/2015).

| Language | Links |
|---|---|
| JavaScript | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/javascript.md#most-starred-repos-javascript) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/javascript.md#most-starred-users-javascript) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/javascript.md#most-starred-orgs-javascript) |
| Java | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/java.md#most-starred-repos-java) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/java.md#most-starred-users-java) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/java.md#most-starred-orgs-java) |
| Python | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/python.md#most-starred-repos-python) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/python.md#most-starred-users-python) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/python.md#most-starred-orgs-python) |
| Objective-C | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/objective-c.md#most-starred-repos-objective-c) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/objective-c.md#most-starred-users-objective-c) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/objective-c.md#most-starred-orgs-objective-c) |
| Swift | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/swift.md#most-starred-repos-swift) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/swift.md#most-starred-users-swift) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/swift.md#most-starred-orgs-swift) |
| Go | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/go.md#most-starred-repos-go) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/go.md#most-starred-users-go) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/go.md#most-starred-orgs-go) |
| PHP | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/php.md#most-starred-repos-php) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/php.md#most-starred-users-php) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/php.md#most-starred-orgs-php) |
| HTML | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/html.md#most-starred-repos-html) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/html.md#most-starred-users-html) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/html.md#most-starred-orgs-html) |
| CSS | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/css.md#most-starred-repos-css) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/css.md#most-starred-users-css) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/css.md#most-starred-orgs-css) |
| Ruby | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/ruby.md#most-starred-repos-ruby) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/ruby.md#most-starred-users-ruby) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/ruby.md#most-starred-orgs-ruby) |
| C++ | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/c++.md#most-starred-repos-c++) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/c++.md#most-starred-users-c++) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/c++.md#most-starred-orgs-c++) |
| C | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/c.md#most-starred-repos-c) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/c.md#most-starred-users-c) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/c.md#most-starred-orgs-c) |
| C# | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/c#.md#most-starred-repos-c#) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/c#.md#most-starred-users-c#) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/c#.md#most-starred-orgs-c#) |
| Shell | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/shell.md#most-starred-repos-shell) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/shell.md#most-starred-users-shell) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/shell.md#most-starred-orgs-shell) |
| Scala | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/scala.md#most-starred-repos-scala) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/scala.md#most-starred-users-scala) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/scala.md#most-starred-orgs-scala) |
| Clojure | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/clojure.md#most-starred-repos-clojure) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/clojure.md#most-starred-users-clojure) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/clojure.md#most-starred-orgs-clojure) |
| Haskell | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/haskell.md#most-starred-repos-haskell) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/haskell.md#most-starred-users-haskell) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/haskell.md#most-starred-orgs-haskell) |
| CoffeeScript | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/coffeescript.md#most-starred-repos-coffeescript) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/coffeescript.md#most-starred-users-coffeescript) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/coffeescript.md#most-starred-orgs-coffeescript) |
| Lua | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/lua.md#most-starred-repos-lua) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/lua.md#most-starred-users-lua) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/lua.md#most-starred-orgs-lua) |
| R | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/r.md#most-starred-repos-r) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/r.md#most-starred-users-r) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/r.md#most-starred-orgs-r) |
| VimL | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/viml.md#most-starred-repos-viml) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/viml.md#most-starred-users-viml) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/viml.md#most-starred-orgs-viml) |
| Perl | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/perl.md#most-starred-repos-perl) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/perl.md#most-starred-users-perl) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/perl.md#most-starred-orgs-perl) |
| Unknown | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/unknown.md#most-starred-repos-unknown) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/unknown.md#most-starred-users-unknown) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/unknown.md#most-starred-orgs-unknown) |
| Overall | [Repos](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/overall.md#most-starred-repos-overall) - [Users](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/overall.md#most-starred-users-overall) - [Orgs](https://github.com/donnemartin/gh-stats/blob/master/language_stats/2015/overall.md#most-starred-orgs-overall) |

## Contributing

Contributions are welcome!

Review the [Contributing Guidelines]() for details on how to:

* Submit issues
* Submit pull requests

## Credits

* [github3.py](https://github.com/sigmavirus24/github3.py) by [Ian Cordasco](https://github.com/sigmavirus24/)
* [Repo header](http://www.clker.com/cliparts/v/P/n/K/B/P/stars-md.png)

## Contact Info

Feel free to contact me to discuss any issues, questions, or comments.

* Email: [donne.martin@gmail.com](mailto:donne.martin@gmail.com)
* Twitter: [donne_martin](https://twitter.com/donne_martin)
* GitHub: [donnemartin](https://github.com/donnemartin)
* LinkedIn: [donnemartin](https://www.linkedin.com/in/donnemartin)
* Website: [donnemartin.com](http://donnemartin.com)

## License

    Copyright 2015 Donne Martin

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
