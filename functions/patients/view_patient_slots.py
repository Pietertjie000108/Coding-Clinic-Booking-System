import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import calender_api
import get_events
import date_format as df
import json
from sys import argv

if __name__ == '__main__':
    service = calender_api.create_auth_service()
    username = argv[1]
    get_events.get_all_code_clinic_slots_to_delete(service, username)