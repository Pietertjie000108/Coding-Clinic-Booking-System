import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import calender_api
import get_events
import date_format as df
import json
import os
from pprint import pprint
from sys import argv

if __name__ == '__main__':
    service = calender_api.create_auth_service()
    username = argv[1]
    events, count = get_events.get_events_for_next_7_days_to_delete(username, service)
    if count == 0:
        print("There are currently no available slots for Code Clinics. Check again later.")

    # page_token = None
    # while True:
    #     calendar_list = service.calendarList().list(pageToken=page_token).execute()
    #     for calendar_list_entry in calendar_list['items']:
    #         pprint(calendar_list_entry)
    #         break
    #         page_token = calendar_list.get('nextPageToken')
    #     if not page_token:
    #         break