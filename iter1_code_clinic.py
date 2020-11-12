import quickstart

def sequence():
    username = input('Please enter your username: ').lower()
    service = quickstart.create_auth_service(username)
    do_clinician = True
    while True:
        if quickstart.is_clinician(username) == True:
            # while True:
            option = quickstart.show_clinician_options(username)
            while option == 1 or option == 2 or option == 3:
                if option == 1:
                    quickstart.get_events_for_next_7_days_to_delete(username)
                if option == 2:
                    quickstart.add_to_calender(service, username)
                if option == 3:
                    quickstart.delete_clinician_slot(service, username)
                option = quickstart.show_clinician_options(username)
        else:
            option = quickstart.show_patient_options(username)
            while option == 1 or option == 2 or option == 3:
                if option == 1:
                    quickstart.get_patient_events_for_next_7_days(username)
                if option == 2:
                    quickstart.add_patient_slot_to_calender(service, username)
                if option == 3:
                    quickstart.delete_clinician_slot(service, username)
                option = quickstart.show_patient_options(username)
    pass

if __name__ == '__main__':
    sequence()
