import datetime
import pandas as pd
from collections import OrderedDict

class LogEntry(object):
    # Object initialization
    def __init__(self):
        date = None
        total_vaccinations = 0


class Country(object):
    # Object initialization
    def __init__(self):
        name = ""
        iso_code = ""
        flag_icon = None
        flag_emoji = None
        population = 0
        population_vaccinated = 0
        entry_list = [] # empty list for entries

    # Function to test if object had been created
    def ping(self):
        print("pong")


class CountryList(object):

    DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv"

    # Object initialization
    def __init__(self):
        CountryList.populate_country_list()

    def populate_country_list():
        df = pd.read_csv(CountryList.DATA_URL)
        print(df.head(5))
        country_list = df['location'].tolist()
        country_dict = OrderedDict.fromkeys(country_list)
        country_list_abbv = list(OrderedDict.fromkeys(country_list)) 
        for element in country_dict:
            print(element)
            country_dict[element] = Country()
            country_dict[element].ping()
        #country_dict = {country_list_abbv:Country()}

    def get_country(country_str):
        try:
            return country_dict[country_str]
        except Error as e:
            print(e)
            return False
