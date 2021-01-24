# COVID Vaccine Twitter Bot
# by Gamal Mohamed
#
#

####################
# IMPORT LIBRARIES #
####################
import multiprocessing
import threading
import sys


##################
# INITIALIZATION #
##################


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
        start_processes()
        # Loop until keyboard interrupt is thrown
        main_loop_flag = True
        while main_loop_flag:
            pass
    # Graceful exit on keyboard interrupt
    except KeyboardInterrupt:
        print()
        end_processes()
        # Exit program
        print("Exiting program.")
        sys.exit(0)
