from __future__ import print_function
from pprint import pprint
import datetime
from datetime import timedelta
import pickle
from calendar import monthrange
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME = 'calender'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']


# SCOPES = ['https://www.googleapis.com/auth/calendar']


def create_auth_service():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return build('calendar', 'v3', credentials=creds)


def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    print(dt)
    return dt


def get_add_to_calender_input():
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

    now = datetime.datetime.now()
    while True:
        month = input('Which month would you like to create a slot for (e.g August): ').lower()
        if month in valid_months:
            break
        else:
            print('Please enter a valid month.')
        
    while True:
        day1 = input('Which day would you like to create a slot for: ')
        day = int(day1)
        if day > 0 and day < monthrange(now.year, valid_months.index(month)+1)[1]:
            break
        else:
            print('Please enter a valid date.')

    while True:
        time = input('What time would you like your slot to be? (9:00 or 15:30): ')
        t = time.split(':')
        if len(t) == 2 and t[0].isdigit and t[1].isdigit and int(t[0]) > 0 and int(t[0]) < 25 and int(t[1]) > -1 and int(t[1]) < 60:
            start = (int(t[0]), int(t[1]))
            a = datetime.datetime(100,1,1,int(t[0]),int(t[1]))
            b = a + timedelta(minutes=30)
            end = (int(b.time().hour), int(b.time().minute))
            break
        else:
            print('Please enter a valid time.')

    return (valid_months.index(month)+1, day, start, end)      


def get_current_and_7_days_date_and_time_in_RFC3339():
    
    date = datetime.datetime.utcnow()
    date_in_7_days = date + timedelta(7)
    date_with_timezone = date.isoformat("T") + "Z"
    date_in_7_days_with_timezone = date_in_7_days.isoformat("T") + "Z"

    return (date_with_timezone, date_in_7_days_with_timezone)


def add_to_calender(service, username):
    colors = service.colors().get().execute()
    d_and_t = get_add_to_calender_input()
    descr = input('Please give a short description of what topics you are willing to help with.')
    event_request_body = {
        'start': {
            'dateTime': convert_to_RFC_datetime(2020, d_and_t[0], d_and_t[1], d_and_t[2][0], d_and_t[2][1]),
            'timeZone': 'Africa/Johannesburg'
        },
        'end': {
            'dateTime': convert_to_RFC_datetime(2020, d_and_t[0], d_and_t[1], d_and_t[3][0], d_and_t[3][1]),
            'timeZone': 'Africa/Johannesburg'
        },
        'summary': f"{username}'s Code Clinic",
        'description': descr,
        # 'colorId': 5,
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
            # {  
            # 'displayName': 'Jason',
            # 'comment': 'I accepted',
            # 'organizer': False,
            # 'email': 'wethinkmock@gmail.com',
            # 'optional': True,
            # 'responseStatus': 'accepted'
            # }
        ]
    }
    
    maxAttendees = 3
    sendNotifications = True
    sendUpdate = 'all'
    # print(event_request_body['start']['dateTime'])
    # print(event_request_body['end']['dateTime'])
    response = service.events().insert(calendarId='primary', sendUpdates='all', body=event_request_body).execute()
    print("Your slot has been created.")
    # pprint(response)


def is_clinician(username):
    while True:
        title = input(f"Hello {username}, do you want to sign-up as a clinician (C) or patient (P)?: ").lower()
        if title == 'c' or title == 'p':
            return title == 'c'
        else:
            print("Please enter either 'C' or 'P'.\n")


def show_clinician_options(username):
    print("These are your current slots: (find a way to add his current slots )\n")
    while True:
        option = input('''What do you want to do next?
> Press [1] to create slot.
> Press [2] to delete a slot.
> Press [3] go back to main menu.\n''')
        if int(option) == 1 or int(option) == 2 or int(option) == 3:
            return int(option)
        else:
            print("Please enter either 1, 2 or 3.")


def get_events_for_next_7_days_to_delete(username):
    time = get_current_and_7_days_date_and_time_in_RFC3339()
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


def actual_delete_events(user_input,username):
    service.events().delete(calendarId='primary', eventId=user_input, sendUpdates='all').execute()
    print(f"\nSlot {user_input} was deleted...")
    print("Here are your current slots.\n")
    events = get_events_for_next_7_days_to_delete(username)


def delete_events(service, username):
    print("These are the slots you've created: \n")
    events = get_events_for_next_7_days_to_delete(username)
    while True:
        user_input = input("Enter the ID of the slot you want to delete: ")
        u_input = (user_input)
        for event in events:
            event_id = event['id']
            if event_id == user_input:
                actual_delete_events(user_input, username)
                return
            if events[-1] == event:
                print("Please enter a valid ID.")


def get_events_for_next_7_days():
    print("- These are your upcoming events for the next 7 days - \n\n")

    time = get_current_and_7_days_date_and_time_in_RFC3339()
    
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


if __name__ == '__main__':
    service = create_auth_service()
    username = input('Please enter your username: ').lower()
    # if is_clinician(username):
    while is_clinician(username):
        option = show_clinician_options(username)
        while option == 1 or option == 2:
            if option == 1:
                add_to_calender(service, username)
            if option == 2:
                delete_events(service, username)
            option = show_clinician_options(username)
    
        events = get_events_for_next_7_days()
        print('Show events and give option to add to events')
    
    # delete_events(service, username)
    # add_to_calender(service)
    # get_current_and_7_days_date_and_time_in_RFC3339()