import datetime
import pandas as pd
from collections import OrderedDict

# Defines a class that represents an log entry from 
class LogEntry(object):
    # Object initialization
    def __init__(self):
        date = None
        total_vaccinations = 0

# Defines a class which represents a country; contains vaccination data
class Country(object):
    # Object initialization
    def __init__(self):
        self.name = ""
        self.iso_code = ""
        self.flag_icon = None
        self.flag_emoji = None
        self.population = 0
        self.population_vaccinated = 0
        self.entry_list = [] # empty list for entries

    # Function to test if object had been created
    def ping(self):
        print("pong")

# Defines a class which contains a list of Country objects
class CountryList(object):

    DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv"

    # Object initialization
    def __init__(self):
        self.country_list = None
        self.country_dict = None
        self.df = self.get_data_frame()
        self.populate_country_list()
        #df = get_data_frame(CountryList.DATA_URL)

    # Pull csv data from GitHub into DataFrame and return
    def get_data_frame(self):
        return pd.read_csv(CountryList.DATA_URL).fillna(0) # Fill empty cells as 0

    # Populate country list and dictionary with country name elements
    # and create Country objects for dictionary
    def populate_country_list(self):
        try:
            self.country_list = self.df['location'].tolist()
            self.country_dict = OrderedDict.fromkeys(self.country_list) # Generate dictionary to remove duplicates and contain Country objects 
            for element in self.country_dict:
                self.country_dict[element] = Country()
            for element in self.country_dict:
                print(element)
                #self.country_dict[element].ping() # Test if object assignment is successful
        except: # Error reading GitHub CSV
            print("There was an error reading the csv from GitHub")

