import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import calender_api
import get_events
import date_format as df
import json
from sys import argv


def update_slot_with_deleted_patient(uid, username, event, service):
    for student in event['attendees']:
        if student['displayName'] == username:
            event['attendees'].remove(student)
    service.events().update(calendarId=get_events.calendar_id, eventId=uid, body=event, sendUpdates='all').execute()
    print(f"You have successfully deleted slot {uid}...\n")


def delete_patient_slot(service, username):
    events, count = get_events.get_all_code_clinic_slots_to_delete_without_printing(service, username)
    if count == 0:
        print("There are currently no available slots to delete.")
        return
    while True:
        uid = argv[2]
        for event in events:
            event_id = event['id']
            if event_id == uid and len(event['attendees']) == 2:
                event2 = service.events().get(calendarId=get_events.calendar_id, eventId=uid).execute()
                # os.remove("patient_files/" + event_id + ".json")
                update_slot_with_deleted_patient(uid, username, event2, service)
                events, count = get_events.get_all_code_clinic_slots_to_delete(service, username)
                if count == 0:
                    print("You don't have anymore slots.")
                    return
                return
            if events[-1] == event:
                print("Please enter a valid ID.")
                return

    
if __name__ == '__main__':
    service = calender_api.create_auth_service()
    username = argv[1]
    delete_patient_slot(service, username)