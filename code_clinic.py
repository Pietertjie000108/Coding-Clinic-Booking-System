import quickstart

def sequence():
    username = input('Please enter your username: ').lower()
    service = quickstart.create_auth_service()
    do_clinician = True
    while True:
        if quickstart.is_clinician(username) == True:
            # while True:
            option = quickstart.show_clinician_options()
            while option == 1 or option == 2 or option == 3 or option == 5:
                if option == 1:
                    quickstart.get_events_for_next_7_days_to_delete(username)
                if option == 2:
                    quickstart.add_to_calender(service, username)
                if option == 3:
                    quickstart.delete_clinician_slot(service, username)
                if option == 5:
                    return False
                option = quickstart.show_clinician_options()
        else:
            option = quickstart.show_patient_options()
            while option == 1 or option == 2 or option == 3 or option == 5:
                if option == 1:
                    quickstart.get_patient_events_for_next_7_days(username)
                if option == 2:
                    quickstart.add_patient_slot_to_calender(service, username)
                if option == 3:
                    quickstart.delete_clinician_slot(service, username)
                if option == 5:
                    return False
                option = quickstart.show_patient_options()
    pass

if __name__ == '__main__':
    sequence()
