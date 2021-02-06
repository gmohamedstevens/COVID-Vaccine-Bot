###################
# Types of tweets #
###################
# Graphic comparing countries (total vaccinations, fully vaccinated)
# ~ Countries putting in their first entry ~
# ~ Total vaccination milestones (1M, 2M, 10M, etc, herd immunity percentages?, ) ~
# ~ Daily vaccination reported ~
# ~ Country information (by request?) ~
# ~ Include a postive interjection (Good job! Nice! Wow! etc) ~
# News articles related to COVID vaccines (auto-detected?)
import math
import random

# https://stackoverflow.com/questions/3154460/python-human-readable-large-numbers
millnames = ['','K','M','B','T']
def millify(n):
    n = float(n)
    millidx = max(0, min(len(millnames)-1, int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

interjection_list = ["Nice", "Way to go", "Awesome", "Good job", "Wow", "Keep it up"]
interjection = random.choice(interjection_list)

##########
# TWEETS #
##########

# String format of country info tweet
str = """{emoji_flag} {country}
Total Vacc.: {tv_count}
Total Fully Vacc.: {tfv_count}
Percent Vacc.: {pv_count}
Percent Fully Vacc.: {pfv_count}
Daily Vacc. Raw: {dvr_count}
Daily Vacc.: {dv_count}""".format(emoji_flag = ":argentina:", country = "Argentina", tv = 0, tfv = 0, pv = 0, pfv = 0, dvr = 0, dv = 0)

# Countries reporting their first entry
str = "{country} recently began reporting vaccination statistics. {interjection}! {emoji_flag}".format(emoji_flag = ":argentina:",
    country = "Argentina", interjection = interjection)

# Milestone tweet (percent and total vaccinations)
count = millify(10000)
str = "{country} reached {count} for reported {stat}. {interjection}! {emoji_flag}".format(emoji_flag = ":argentina:",
    stat = "Total Fully Vaccinated", count = count, country = "Argentina", interjection = interjection)

# Daily report (daily vaccinations)
str = "{country} reported {count} vaccinations were made on {date}. {emoji_flag}".format(emoji_flag = ":argentina:",
    stat = "Total Fully Vaccinated", count = count, country = "Argentina", interjection = interjection raw = "(raw)")

print(str)
