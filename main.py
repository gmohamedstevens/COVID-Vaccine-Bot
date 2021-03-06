# COVID Vaccine Twitter Bot
# by Gamal Mohamed

####################
# IMPORT LIBRARIES #
####################
import multiprocessing
import sys
import tweepy
from location import *
from bot import *

##################
# INITIALIZATION #
##################
location_list = LocationList()
twitter_bot = TwitterBot()

#############
# PROCESSES #
#############
def gather_vaccine_data():
    while True:
        pass
process_vaccine_data = multiprocessing.Process(target=gather_vaccine_data)

def start_processes():
    # Start vaccine data collection process
    process_vaccine_data.start()
    print("Vaccination data collection process started.")

def end_processes():
    # Terminate vaccine data collection process
    process_vaccine_data.terminate()
    process_vaccine_data.join()
    print("Vaccination data collection process ended.")

#####################
# MAIN PROGRAM LOOP #
#####################
if __name__ == '__main__':
    try:
        print("Program started.")
        # start_processes()
        # Loop until keyboard interrupt is thrown
        main_loop_flag = True
        while main_loop_flag:
            pass
    # Graceful exit on keyboard interrupt
    except KeyboardInterrupt:
        # end_processes()
        # Exit program
        twitter_bot.set_description(Status.OFFLINE)
        print("Exiting program.")
        sys.exit(0)
