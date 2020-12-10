import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import connection_test as ct
import calender_api
import get_events
import auth_interface
import json
from sys import argv


def main_function():
    if ct.connection_test() == True:
        if auth_interface.check_if_credentials_have_expired():
            return
        service = calender_api.create_auth_service()
        username = get_events.get_username()
        events, count = get_events.get_all_code_clinic_slots_to_signup(service, username)
        if count == 0:
            print("There are currently no available slots for Code Clinics. Check again later.")
    else :
        print("\nPlease check your internet connection. \n")
        return


if __name__ == '__main__':
    main_function()