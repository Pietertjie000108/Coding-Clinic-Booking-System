from functions import date_format as df
import json
import os

"""
clinician functs
"""
def create_events_from_service(service):
    """
    creating/ getting events from the google api
    if no events are found it shows no upcoming events.
    else ir returns any events present.
    """
    time = df.get_current_and_7_days_date_and_time_in_RFC3339()
    events_result = service.events().list(calendarId='primary', timeMin=time[0],
                                        singleEvents=True, timeMax=time[1],
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    return events


# def get_all_code_clinic_slots(service):
#     """
#     """
#     print("These are all the available slots you can choose from.\n")
#     events = create_events_from_service(service)
#     for event in events:
#         start = event['start'].get('dateTime', event['start'].get('date'))
#         items_list =  event['attendees']
#         if len(items_list) == 1:
#             print(f"""Date: {start}
# Summary: {event['summary']}
# ID: {event['id']}\n""")
#     return events


def add_to_calender(service, username):
    """
    Adding an event to Google Calendar using the format the calendar uses when setting up an event.
    using the user input from (get_add_to_calendar_input) 
    also stores a .json file in data_files
    """
    colors = service.colors().get().execute()
    d_and_t = df.get_add_to_calender_input()
    descr = input('Please give a short description of what topics you are willing to help with: ')
    event_request_body = {
        'start': {
            'dateTime': df.convert_to_RFC_datetime(2020, d_and_t[0], d_and_t[1], d_and_t[2][0]-2, d_and_t[2][1]),
            'timeZone': 'Africa/Johannesburg'
        },
        'end': {
            'dateTime': df.convert_to_RFC_datetime(2020, d_and_t[0], d_and_t[1], d_and_t[3][0]-2, d_and_t[3][1]),
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
            'responseStatus': 'accepted'
            }
        ]
    }
    
    maxAttendees = 3
    sendNotifications = True
    sendUpdate = 'all'
    response = service.events().insert(calendarId='primary', sendUpdates='all', body=event_request_body).execute()
    print("\nYour slot has been created...\n")
    with open('clinician_files/'+response['id']+'.json', 'w+') as outfile:
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
    count = 0
    for event in events:
        start = df.format_time_to_make_readable(event)
        description = event['description']
        if event['summary'] == f'{username} - Code Clinic':
            count = 1
            print(f"""Date: {start}
Summary: {event['summary']}
Description: {description}
ID: {event['id']}\n""")
    return events, count


def actual_delete_events(user_input, username, service):
    service.events().delete(calendarId='primary', eventId=user_input, sendUpdates='all').execute()
    print(f"\nSlot {user_input} was deleted...")
    events, count = get_events_for_next_7_days_to_delete(username, service)
    return events, count


def delete_clinician_slot(service, username):
    events, count = get_events_for_next_7_days_to_delete(username, service)
    if count == 0:
        print("There are currently no available slots to delete.")
        return
    while True:
        user_input = input("Enter the ID of the slot you want to delete: ")
        for event in events:
            event_id = event['id']
            if event_id == user_input:
                events1, count1 = actual_delete_events(user_input, username, service)
                os.remove("clinician_files/" + event_id + ".json")
                if count1 == 0:
                    print("There are currently no available slots to delete.")
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
        start = df.format_time_to_make_readable(event)
        end = event['end'].get('dateTime', event['start'].get('date'))
        print(f"Starts at: {start}, and ends at: {end} you must: {event['summary']}")