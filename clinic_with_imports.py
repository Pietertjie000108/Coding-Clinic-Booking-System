from functions import google_calendar_api
from functions import user_check
from functions import clinicians
from functions import patients


def initialize_user_token():
 
    google_calendar_api.cred_gen()


def clinician_options(username, service):
    option = user_check.show_clinician_options()
    while option == 1 or option == 2 or option == 3:
        if option == 1:
            clinicians.get_events_for_next_7_days_to_delete(username, service)
        if option == 2:
           clinicians.add_to_calender(service, username)
        if option == 3:
            clinicians.delete_clinician_slot(service, username)
        option = user_check.show_clinician_options()


def patient_options(username, service):
    option = user_check.show_patient_options()
    while option == 1 or option == 2 or option == 3:
        if option == 1:
            patients.get_patient_events_for_next_7_days(username, service)
        if option == 2:
            patients.add_patient_slot_to_calender(service, username)
        if option == 3:
            patients.delete_patient_slot(service, username)
        option = user_check.show_patient_options()


def main():
    username = input('Please enter your username: ').lower()
    initialize_user_token()
    service = google_calendar_api.service_gen()
    while True:
        if user_check.is_clinician(username) == True:
            clinician_options(username, service)
        else :
            patient_options(username, service)


if __name__ == '__main__':
    main()