from datetime import datetime, timedelta
from google_auth_oauthlib.helpers import credentials_from_session
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path

start_time = datetime(2020, 11, 7, 10, 15, 0)
end_time = start_time + timedelta(hours=1, minutes=30)

scopes = ['https://www.googleapis.com/auth/calendar']
def main():

    creds = None
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

    service = build("calendar", "v3", credentials = creds)

    # results = service.calendarList().list().execute()
    # calendar_Id = results['items'][0]
    events_result = service.events().list(calendarId='primary', timeZone = 'South Africa',).execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['id'])
    service.events().delete(calendarId='primary', eventId='7jjjhmb82tmb8l15sa12m28lqo').execute()
#     event = {
#   'summary': 'Test slot making',
#   'location': 'Cape Town',
#   'description': 'testing bros.',
#   'start': {
#     'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
#     'timeZone': 'Africa/Johannesburg',
#   },
#   'end': {
#     'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
#     'timeZone': 'Africa/Johannesburg',
#   },
#   'recurrence': [
#     'RRULE:FREQ=DAILY;COUNT=5'
#   ],
#   'reminders': {
#     'useDefault': False,
#     'overrides': [
#       {'method': 'email', 'minutes': 24 * 60},
#       {'method': 'popup', 'minutes': 10},
#     ],
#   },
# }

#     event = service.events().insert(calendarId="primary", body=event).execute()
        
if __name__ == '__main__':
    main()