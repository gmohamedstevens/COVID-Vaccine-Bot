# Sources:
# https://www.pythoncentral.io/introduction-to-tweepy-twitter-for-python/
# https://realpython.com/twitter-bot-python-tweepy/
# https://www.pythoncentral.io/introduction-to-tweepy-twitter-for-python/

import tweepy
from enum import Enum
import twitter_config as tc

# Enumeration of status states
class Status(Enum):
        ONLINE = 1
        OFFLINE = 2

# Creates a Twitter bot
class TwitterBot(object):
    
    STATUS_DICT = {
            Status.ONLINE: "Online 🟢",
            Status.OFFLINE: "Offline 🔴"
        }
    
    # Object initialization
    def __init__(self):
        # OAuth process, using the keys and tokens
        self.AUTH = tweepy.OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
        self.AUTH.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)
        # Creation of the actual interface, using authentication
        self.API = tweepy.API(self.AUTH)
        try:
            self.API.verify_credentials()
            print("Twitter Authentication OK")
            self.set_description(Status.ONLINE) # Set status to online
        except:
            print("Error during authentication")
    
    def set_description(self, status):
        msg = TwitterBot.STATUS_DICT[status]
        print(msg)
        self.API.update_profile(description = msg) 

