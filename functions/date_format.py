import datetime
from datetime import timedelta
from calendar import monthrange
import re

"""
Data formats
"""
def format_time_to_make_readable(event):
    start1 = event['start'].get('dateTime', event['start'].get('date'))
    start = re.split("[-T:+]",start1)
    return f'{start[0]}-{start[1]}-{start[2]} @ {start[3]}:{start[4]}'


def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt


def get_current_and_7_days_date_and_time_in_RFC3339():
    
    date = datetime.datetime.utcnow()
    date_in_7_days = date + timedelta(7)
    date_with_timezone = date.isoformat("T") + "Z"
    date_in_7_days_with_timezone = date_in_7_days.isoformat("T") + "Z"

    return (date_with_timezone, date_in_7_days_with_timezone)


def get_add_to_calender_input():
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

    now = datetime.datetime.now()
    while True:
        month = input('\nWhich month would you like to create a slot for (e.g August): ').lower()
        if month in valid_months:
            break
        else:
            print('Please enter a valid month.')
        
    while True:
        day1 = input('Which day would you like to create a slot for: ')
        day = int(day1)
        if day > 0 and day <= monthrange(now.year, valid_months.index(month)+1)[1]:
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

