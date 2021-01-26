### COVID Vaccination Twitter Bot
###### By Gamal Mohamed

**Description:** A Twitter bot that pulls world COVID vaccination records from a GitHub source and tweets comparisons and fun facts of country progress

***
#### Python Dependencies & Libraries
- *Tweepy* - For accessing Twitter API and handling Tweeting functions
- *pandas* - For reading csv from GitHub and to provide data processing
- *collecitons* - For the OrderedDict class; for getting the list of counries from the GitHub csv
- *enum* - Enumeration of tweet types and status

***
#### Accomplished So Far
- Pulls data from GitHub CSV and parses list of countries
- Able to update status using authentication keys

***
#### Planned Features
- Get total population data from trusted source
- Analyze log entries for tweetable facts
- Generate bar chart comparing country vaccination progress (per 100 citizens)
- Tweet on behalf of another account (oAuth?)
