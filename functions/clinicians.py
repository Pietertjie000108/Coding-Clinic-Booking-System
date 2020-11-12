from functions import date_format as df
import json
import os

"""
clinician functs
"""
def create_events_from_service(service):
    time = df.get_current_and_7_days_date_and_time_in_RFC3339()
    events_result = service.events().list(calendarId='primary', timeMin=time[0],
                                        singleEvents=True, timeMax=time[1],
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    return events

def get_all_code_clinic_slots(service):
    print("These are all the available slots you can choose from.\n")
    events = create_events_from_service(service)
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        items_list =  event['attendees']
        if len(items_list) == 1:
            print(f"""Date: {start}
Summary: {event['summary']}
ID: {event['id']}\n""")
    return events


def add_to_calender(service, username):
    #colors = service.colors().get().execute()
    d_and_t = df.get_add_to_calender_input()
    descr = input('Please give a short description of what topics you are willing to help with: ')
    event_request_body = {
        'start': {
            'dateTime': df.convert_to_RFC_datetime(2020, d_and_t[0], d_and_t[1], d_and_t[2][0], d_and_t[2][1]),
            'timeZone': 'Africa/Johannesburg'
        },
        'end': {
            'dateTime': df.convert_to_RFC_datetime(2020, d_and_t[0], d_and_t[1], d_and_t[3][0], d_and_t[3][1]),
            'timeZone': 'Africa/Johannesburg'
        },
        'summary': f"{username} - Code Clinic",
        'description': descr,
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
            }
        ]
    }
    
    maxAttendees = 3
    sendNotifications = True
    sendUpdate = 'all'
    response = service.events().insert(calendarId='primary', sendUpdates='all', body=event_request_body).execute()
    with open('data_files/'+response['id']+'.json', 'w+') as outfile:
        json.dump(response, outfile, sort_keys=True, indent=4)
    print("\nYour slot has been created...\n")
    get_events_for_next_7_days_to_delete(username, service)


def get_events_for_next_7_days_to_delete(username, service):
    print("These are your current slots: \n")
    time = df.get_current_and_7_days_date_and_time_in_RFC3339()
    events_result = service.events().list(calendarId='primary', timeMin=time[0],
                                        singleEvents=True, timeMax=time[1],
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        if event['summary'] == f'{username} - Code Clinic':
            print(f"""Date: {start}
Summary: {event['summary']}
ID: {event['id']}\n""")
    return events


def actual_delete_events(user_input, username, service):
    service.events().delete(calendarId='primary', eventId=user_input, sendUpdates='all').execute()
    print(f"\nSlot {user_input} was deleted...")
    # print("Here are your current slots.\n")
    events = get_events_for_next_7_days_to_delete(username, service)


def delete_clinician_slot(service, username):
    print("These are the slots you've created: \n")
    events = get_events_for_next_7_days_to_delete(username, service)
    while True:
        user_input = input("Enter the ID of the slot you want to delete: ")
        for event in events:
            event_id = event['id']
            if event_id == user_input:
                actual_delete_events(user_input, username, service)
                os.remove(f"data_files/" + user_input + ".json")
                return
            if events[-1] == event:
                print("Please enter a valid ID.")


def get_events_for_next_7_days(service):
    print("- These are your upcoming events for the next 7 days - \n\n")

    time = df.get_current_and_7_days_date_and_time_in_RFC3339()
    
    events_result = service.events().list(calendarId='primary', timeMin=time[0],
                                        singleEvents=True, timeMax=time[1],
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['start'].get('date'))
        print(f"Starts at: {start}, and ends at: {end} you must: {event['summary']}")
    # pprint(events)