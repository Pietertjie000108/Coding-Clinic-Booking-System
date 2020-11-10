from datetime import datetime, timedelta
import json
from google_auth_oauthlib.helpers import credentials_from_session
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path

creds = None
scopes = ['https://www.googleapis.com/auth/calendar.events']
service = None

valid_months = ['january', 'february','march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
valid_check = ['1', '2', '3', '4']

def cred_gen(username):
    global creds
    if os.path.exists('tokens/'+username+'.pickle'):
        with open('tokens/'+username+'.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials/client_secret.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('tokens/'+username+'.pickle', 'wb') as token:
            pickle.dump(creds, token)


def service_gen():
    global service
    service = build('calendar', 'v3', credentials=creds)


def remove_event(event_id):
    global service
    service.events().delete(calendarId='primary', eventId= event_id, sendUpdates='all').execute()
    event_data_removal(event_id)
    print(event_id + ' deleted succesfully')


def show_event_id():
    events_result = service.events().list(calendarId='primary',).execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    else :
        print("These are your events")
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['id'])
            # with open('data_files/events.json', 'a+') as json_file:
            #     json.dump(event, json_file, sort_keys=True, indent=4)
            # json_file.close()



def create_event_voluteer_slots(summary_res, desc, location, vol, start, end):
    event = {
  'summary': summary_res,
  'location': location,
  'description': desc,
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
    with open('data_files/'+event['id']+'.json', 'w+') as outfile:
        json.dump(event, outfile, sort_keys=True, indent=4)


def summary_check(username):
    summary_res = 'Code Clinic - ' + str(username)
    return summary_res


def location_input():
    loc = input("Location? ")
    return loc


def desc_input():
    desc = input("What topics can you assist with?")
    return desc


def user_email(username):
    email = username + "@student.wethinkcode.co.za"
    return email


def time_slot_volunteer():
    year = 2020
    month = int(month_check())
    day = int(input("what day would you like to book the time slot: "))
    hours = int(input("what time would you like to book the time slot? (HOUR): "))
    minutes = int(input("what time would you like to book the time slot? (MINUTE): "))
    second = 0
    return (year,month,day,hours,minutes,second)


def month_validate(month):
    if month.lower() == 'january':
        return '1'
    elif month.lower() == 'february':
        return '2'
    elif month.lower() == 'march':
        return '3'
    elif month.lower() == 'april':
        return '4'
    elif month.lower() == 'may':
        return '5'
    elif month.lower() == 'june':
        return '6'
    elif month.lower() == 'july':
        return '7'
    elif month.lower() == 'august':
        return '8'
    elif month.lower() == 'september':
        return '9'
    elif month.lower() == 'october':
        return '10'
    elif month.lower() == 'november':
        return '11'
    elif month.lower() == 'december':
        return '12'


def month_check():
    month = input("What month would you like to book the time slot: ")
    if month.lower() in valid_months:
        return month_validate(month)
    elif month.lower not in valid_months:
        month = input("enter valid month: ")
        return month_validate(month)
        

def user_input():
    check = input("Code Clinic Tool:\n 1) Book a slot: \n 2) Create a slot: \n 3) delete a slot: \n 4) Display events: \n Pick a number: ")
    if check in valid_check:
        if check == '1':
            return 'student'
        elif check == '2':
            return 'create'
        elif check == '3':
            return 'delete'
        elif check == '4':
            return 'events'


def event_data_removal(event_id):
    with open('data_files/'+ str(event_id) +'.json', 'r+') as json_file:
        update = None
        with open('data_files/'+ str(event_id) +'.json', 'w') as outfile:
            json.dump(update, outfile, sort_keys=True, indent=4)
        json_file.close()
        outfile.close()
    os.remove("data_files/" + event_id + ".json")


def command_handler(command, username):
    if command == "student":
    # attendee_booking(event_id)
        pass
    elif command == "delete":
        # event_log()
        event_id = input("What event would you like to delete? ")
        remove_event(event_id)
    elif command == 'events':
        show_event_id()
        #existing_events()
    else :
        summary = summary_check(username)
        loc = location_input()
        vol = user_email(username)
        desc = desc_input()
        start_time_volunteer = time_slot_volunteer()
        year,month,day,hour,minute,second = start_time_volunteer
        date = datetime(year,month,day,hour,minute,second)
        end_time_volunteer = date + timedelta(hours=0, minutes=30)
        # print (date)
        # print (end_time_volunteer)
        # desc = desc_input()
        create_event_voluteer_slots(summary, desc, loc, vol, date, end_time_volunteer)


def main():
    username = input("What is your username?")
    cred_gen(username)
    service_gen()
    command = user_input()
    command_handler(command, username)



if __name__ == '__main__':
    main()