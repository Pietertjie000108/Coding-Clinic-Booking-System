from functions import google_calendar_api
from functions import user_check
from functions import clinicians
from functions import patients


def initialize_user_token():
    """
    generates token for api
    """
    google_calendar_api.cred_gen()


def clinician_options(username, service):
    """
    executes the clinicians functions depending on input
    """
    option = user_check.show_clinician_options()
    while option == 1 or option == 2 or option == 3 or option == 5:
        if option == 1:
            events, count = clinicians.get_events_for_next_7_days_to_delete(username, service)
            if count == 0:
                print("You currently don't have any slots.\n")
        if option == 2:
           clinicians.add_to_calender(service, username)
        if option == 3:
            clinicians.delete_clinician_slot(service, username)
        if option == 5:
            return False
        option = user_check.show_clinician_options()


def patient_options(username, service):
    """
    executes the patients functions depending on input
    """
    option = user_check.show_patient_options()
    while option == 1 or option == 2 or option == 3 or option == 5:
        if option == 1:
            patients.get_patient_events_for_next_7_days(username, service)
        if option == 2:
            patients.add_patient_slot_to_calender(service, username)
        if option == 3:
            patients.delete_patient_slot(service, username)
        if option == 5:
            return False
        option = user_check.show_patient_options()


def main():
    username = input('Please enter your username: ').lower()
    initialize_user_token()
    service = google_calendar_api.service_gen()
    while True:
        if user_check.is_clinician(username) == True:
            clinician_system = clinician_options(username, service)
            if clinician_system == False:
                return
        else :
            patient_system = patient_options(username, service)
            if patient_system == False:
                return


if __name__ == '__main__':
    main()