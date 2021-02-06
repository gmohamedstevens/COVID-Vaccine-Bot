### COVID Vaccination Twitter Bot (@covacc_global & @covacc_usa)
###### By Gamal Mohamed

**Description:** A Twitter bot that pulls world COVID vaccination records from a GitHub source and tweets comparisons and fun facts of country progress

***
#### Python Dependencies & Libraries
- *Python v3.9*
- *Tweepy* - For accessing Twitter API and handling Tweeting functions
- *pandas* - For reading csv from GitHub and to provide data processing
- *collections* - For the OrderedDict class; for getting the list of counries from the GitHub csv
- *enum* - Enumeration of tweet types and status
- *Requests-OAuthlib* - Perform oAuth authentication for bot accounts
- *emoji-country-flag* - Get country flag emoji to add pizzazz to tweets (using v1.2.3)

***
#### Accomplished So Far
- Pulls data from GitHub CSV and parses list of countries
- Uses authentication keys for account access (tweets, profile changes, etc.)
- oAuth handling for tweeting on behalf of bot account (@covacc_global and @covacc_usa)

***
#### Planned Features
- Get total population data from trusted source
- Analyze log entries for tweetable facts
- Generate bar chart comparing country vaccination progress (per 100 citizens)
- Begin tweeting!
- Automatically retweet articles related to the COVID vaccine? Or maybe retweeting articles in a semi-supervised fashion
