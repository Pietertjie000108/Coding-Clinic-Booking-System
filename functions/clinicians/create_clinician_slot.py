import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import calender_api
import get_events
import date_format as df
import json
import datetime
import os
from sys import argv


def check_if_slots_overlap(start, end, service, username):
    events_result = service.events().list(calendarId=get_events.calendar_id, timeMin=start,
                                        singleEvents=True, timeMax=end,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        return True
    return False


def add_to_calender(service, username):
    """[Adding an event to Google Calendar by saving all the info for that event to an event request body ]

    Args:
        service ([object]): [the service object that will allow us to add events to the calender]
        username ([string]): [students username]
    """    
    colors = service.colors().get().execute()
    d_and_t = df.get_add_to_calender_input(argv[2], argv[3], argv[4])
    now = datetime.datetime.now()
    if d_and_t == None:
        return
    event_request_body = {
        'start': {
            'dateTime': df.convert_to_RFC_datetime(now.year, d_and_t[0], d_and_t[1], d_and_t[2][0]-2, d_and_t[2][1]),
            'timeZone': 'Africa/Johannesburg'
        },
        'end': {
            'dateTime': df.convert_to_RFC_datetime(now.year, d_and_t[0], d_and_t[1], d_and_t[3][0]-2, d_and_t[3][1]),
            'timeZone': 'Africa/Johannesburg'
        },
        'summary': f"{username} - Code Clinic",
        'description': 'empty',
        'status': 'confirmed',
        'transparency': 'opaque',
        'visibility': 'public',
        'location': 'WTC',
        'guestsCanModify': True,
        'attendees': [
            {  
            'displayName': username,
            'organizer': True,
            'email': f'{username}@student.wethinkcode.co.za',
            'optional': True,
            'responseStatus': 'accepted'
            }
        ]
    }
    start = event_request_body['start']['dateTime']
    end = event_request_body['end']['dateTime']
    overlaps = check_if_slots_overlap(start, end, service, username)
    if overlaps:
        response = service.events().insert(calendarId=get_events.calendar_id, sendUpdates='all', body=event_request_body).execute()
        print("\nYour slot has been created...\n")
        event_id = response['id']
        with open('clinician_files/' + event_id + '.json', 'w+') as outfile:
            json.dump(response, outfile, sort_keys=True, indent=4)
            outfile.close()
    else:
        print("You've already created a slot for this time. Please choose another time...")
    events, count = get_events.get_events_for_next_7_days_to_delete(username, service)
    if count == 0:
        print("There are currently no available slots for Code Clinics. Check again later.")
        return

if __name__ == '__main__':
    service = calender_api.create_auth_service()
    username = argv[1]
    add_to_calender(service, username)
