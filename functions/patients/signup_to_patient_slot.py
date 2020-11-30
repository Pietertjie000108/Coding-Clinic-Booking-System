import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import calender_api
import get_events
import date_format as df
import json
from sys import argv

def update_slot_with_patient(uid, username, event, service):
    descr = argv[2]
    if len(event['attendees']) == 2:
        print(f"\nThe slot you tried signing up for is already taken. Please choose another slot.")
        return
    response = {'displayName': username,
    'email': f'{username}@student.wethinkcode.co.za',
    'optional': True,
    'responseStatus': 'accepted',
    'description': descr,
    }
    event['attendees'].append(response)
    service.events().update(calendarId=get_events.calendar_id, eventId=uid, body=event, sendUpdates='all').execute()
    print(f"\nYou have successfully signed up for {event['summary']}...")


def add_patient_slot_to_calender(service, username):
    events, count = get_events.get_all_code_clinic_slots_to_signup_without_printing_anything(service, username)
    while True:
        uid = argv[3]
        for event in events:
            event_id = event['id']
            if event_id == uid:
                event2 = service.events().get(calendarId=get_events.calendar_id, eventId=uid).execute()
                update_slot_with_patient(uid, username, event2, service)
                get_events.get_all_code_clinic_slots_to_delete(service, username)
                with open("functions/patient/patient_files/"+ event_id +'.json', 'w+') as outfile:
                    json.dump(event2, outfile, sort_keys=True, indent=4)
                    outfile.close()
                return
            if events[-1] == event:
                print("Please enter a valid ID.")
                return


if __name__ == '__main__':
    service = calender_api.create_auth_service()
    username = argv[1]
    add_patient_slot_to_calender(service, username)