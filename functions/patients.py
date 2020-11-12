from functions import date_format as df

"""
patient functs
"""
def get_all_code_clinic_slots_to_signup(service, username):
    print("These are all the available slots you can choose from.\n")
    events = create_events_from_service(service)
    count = 0
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        items_list =  event['attendees']
        if len(items_list) == 1 and username not in event['summary']:
            count = 1
            print(f"""Date: {start}
Summary: {event['summary']}
ID: {event['id']}\n""")
    return events, count


def create_events_from_service(service):
    time = df.get_current_and_7_days_date_and_time_in_RFC3339()
    events_result = service.events().list(calendarId='primary', timeMin=time[0],
                                        singleEvents=True, timeMax=time[1],
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    return events


def get_all_code_clinic_slots_to_delete(service, username):
    print("These are all the available slots you can choose from.\n")
    events = create_events_from_service(service)
    count = 0
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        items_list =  event['attendees']
        if len(items_list) == 2:
            items_dict = items_list[0]
            items_dict2 = items_list[1]
        else:    
            items_dict = items_list[0]
            items_dict2 = {'displayName': 'placeholder'}
        if (items_dict['displayName'] == username or items_dict2['displayName'] == username) and username not in event['summary']:
            count = 1
            print(f"""Date: {start}
Summary: {event['summary']}
ID: {event['id']}\n""")
    return events, count


def update_slot_with_patient(uid, username, event, service):
    response = {'displayName': username,
    'email': f'{username}@student.wethinkcode.co.za',
    'optional': True,
    'responseStatus': 'accepted'
    }
    event['attendees'].append(response)
    service.events().update(calendarId='primary', eventId=uid, body=event, sendUpdates='all').execute()
    print(f"\nYou have successfully signed up for {event['summary']}...")
   

def update_slot_with_deleted_patient(uid, username, event, service):
    for student in event['attendees']:
        if student['displayName'] == username:
            event['attendees'].remove(student)
    service.events().update(calendarId='primary', eventId=uid, body=event, sendUpdates='all').execute()
    

def add_patient_slot_to_calender(service, username):
    events, count = get_all_code_clinic_slots_to_signup(service, username)
    if count == 0:
        print("There are currently no available slots for Code Clinics. Check again later.")
        return
    
    while True:
        uid = input("Which Code Clinic slot would you like to sign-up to: ")
        for event in events:
            event_id = event['id']
            if event_id == uid:
                event2 = service.events().get(calendarId='primary', eventId=uid).execute()
                update_slot_with_patient(uid, username, event2, service)
                get_patient_events_for_next_7_days(username, service)
                return
            if events[-1] == event:
                print("Please enter a valid ID.")


def delete_patient_slot(service, username):
    events, count = get_all_code_clinic_slots_to_delete(service, username)
    if count == 0:
        print("There are currently no available slots to delete.")
        return
    while True:
        uid = input("Which Code Clinic slot would you like to delete: ")
        for event in events:
            event_id = event['id']
            if event_id == uid:
                event2 = service.events().get(calendarId='primary', eventId=uid).execute()
                update_slot_with_deleted_patient(uid, username, event2, service)
                events, count = get_all_code_clinic_slots_to_delete(service, username)
                if count == 0:
                    print("There are currently no available slots to delete.")
                    return
            if events[-1] == event:
                print("Please enter a valid ID.")


def get_patient_events_for_next_7_days(username, service):
    print("These are the clinics you've signed up for: \n")
    time = df.get_current_and_7_days_date_and_time_in_RFC3339()
    events_result = service.events().list(calendarId='primary', timeMin=time[0],
                                        singleEvents=True, timeMax=time[1],
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    # pprint(events)
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        items_list =  event['attendees']
        items_dict = items_list[0]
        if items_dict['displayName'] == username and username not in event['summary']:
            print(f"""Date: {start}
Summary: {event['summary']}
ID: {event['id']}\n""")
