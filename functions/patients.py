from functions import date_format as df

"""
patient functs
"""
# def update_slot_with_patient(user_input, username, event, service):
#     start = event['start'].get('dateTime', event['start'].get('date'))
#     start = event['end'].get('dateTime', event['start'].get('date'))
#     # event_request_body = 


# def add_patient_slot_to_calender(service, username):
#     get_all_code_clinic_slots(service)
#     uid = input("Which Code Clinic slot would you like to sign-up to: ")
#     for event in events:
#         event_id = event['id']
#         if event_id == user_input:
#             update_slot_with_patient(user_input, username, event, service)
#             return
#         if events[-1] == event:
#             print("Please enter a valid ID.")



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
