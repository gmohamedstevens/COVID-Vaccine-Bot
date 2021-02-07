import datetime
import pandas as pd
from collections import OrderedDict

# Defines a class that represents an log entry from
class LogEntry(object):
    # Object initialization
    def __init__(self):
        self.date = None
        self.tv_count = 0 # Total vaccinations
        self.pv_count = 0 # People vaccinated
        self.pfv_count = 0 # People fully vaccinated
        self.dv_count = 0 # Daily vaccinations
        self.dvr_count = 0 # Daily vaccinations (raw)
        self.tv_percent = 0 # Total vaccinations
        self.pv_percent = 0 # Percent people vaccinated
        self.pfv_percent = 0 # Percent people fully vacciated

    def flatten(self):
        pass

# Defines a class which represents a location; contains vaccination data
class Location(object):
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

# Defines a class which contains a list of Location objects
class LocationList(object):

    DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv"

    # Object initialization
    def __init__(self):
        self.country_list = None
        self.previous_list = None
        self.country_dict = None
        self.df = self.get_data_frame()
        self.populate_location_list()
        #df = get_data_frame(CountryList.DATA_URL)

    # Pull csv data from GitHub into DataFrame and return
    def get_data_frame(self):
        return pd.read_csv(LocationList.DATA_URL).fillna(0) # Fill empty cells as 0

    # Populate location list and dictionary with country name elements
    # and create Location objects for dictionary
    def populate_location_list(self):
        try:
            self.previous_list = self.location_list # Store previous list for testing if a new country has began to report data
            self.location_list = self.df['location'].tolist()
            self.location_dict = OrderedDict.fromkeys(self.location_list) # Generate dictionary to remove duplicates and contain Country objects
            for location in self.location_dict:
                self.location_dict[country] = Location()
        except: # Error reading GitHub CSV
            print("There was an error reading the csv from GitHub")

    # Shuffles order of locations in list
    def shuffle_location_list_order():
        pass
