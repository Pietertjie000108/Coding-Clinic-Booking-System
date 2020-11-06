from datetime import datetime, timedelta
from google_auth_oauthlib.helpers import credentials_from_session
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path

creds = None
scopes = ['https://www.googleapis.com/auth/calendar.events']



def cred_gen():
    global creds
    if os.path.exists('token.pickle'): 
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token) 
    if not creds or not creds.valid:                                                                # If there are no (valid) credentials available, let the user log in.
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes = scopes)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:                                                   #Save the credentials for the next run
            pickle.dump(creds, token)


def service_gen():
    global service
    service = build('calendar', 'v3', credentials=creds)


def remove_event(event_id):
    global service
    service.events().delete(calendarId='primary', eventId= event_id).execute()


def show_event_id():
    events_result = service.events().list(calendarId='primary', timeZone = 'South Africa',).execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['id'])


def create_event_voluteer_slots(summary_res, location, vol, start, end):
    event = {
  'summary': summary_res,
  'location': location,
  'description': 'Coding Clinic that students can book to get assistance with any questions they have.',
  'start': {
    'dateTime': start.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': 'Africa/Johannesburg',
  },
  'end': {
    'dateTime': end.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': 'Africa/Johannesburg',
  },
  'attendees': [
    {'email': vol}
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

    event = service.events().insert(calendarId="primary", body=event).execute()


def summary_input():
    summary_res = input("What is your username for the time slot? ")
    return summary_res


def location_input():
    loc = input("are you at WTC or W17? ")
    return loc


def desc_input():
    desc = input("What would you like the code clinic to deal with?")
    return desc


def user_email():
    user = input("Please enter your email address: ")
    return user


def time_slot_volunteer():
    year = 2020
    month = int(input("What month would you like to book the time slot: "))
    day = int(input("what day would you like to book the time slot: "))
    hours = int(input("what time would you like to book the time slot? (HOUR): "))
    minutes = int(input("what time would you like to book the time slot? (MINUTE): "))
    second = 0
    return (year,month,day,hours,minutes,second)


def volunteer_or_student():
    check = input("Do you want to create a slot or book a slot? (create or book): ")
    if check.lower() == "book":
        return "student"
    elif check.lower() == "create":
        return "volunteer"

def main():
    cred_gen()
    service_gen()
    show_event_id()
    if volunteer_or_student() == "student":
        pass
    else :
        summary = summary_input()
        loc = location_input()
        vol = user_email()
        start_time_volunteer = time_slot_volunteer()
        year,month,day,hour,minute,second = start_time_volunteer
        date = datetime(year,month,day,hour,minute,second)
        end_time_volunteer = date + timedelta(hours=1, minutes=30)
        # print (date)
        # print (end_time_volunteer)
        # desc = desc_input()
        create_event_voluteer_slots(summary, loc, vol, date, end_time_volunteer)
if __name__ == '__main__':
    main()