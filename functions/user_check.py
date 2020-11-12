def is_clinician(username):
    while True:
        title = input(f"Hello {username}, do you want to sign-up as a clinician (C) or patient (P)?: ").lower()
        if title == 'c' or title == 'p':
            return title == 'c'
        else:
            print("Please enter either 'C' or 'P'.\n")


def show_patient_options():
    while True:
        print('''What do you want to do next?
> Press [1] to view clinics you've signed up for.
> Press [2] to signup to a clinic slot.
> Press [3] to delete clinic slot.
> Press [4] go back to main menu.
> Press [5] to turn off program.\n''')
        option = input("Enter your option here: ")
        if int(option) == 1 or int(option) == 2 or int(option) == 3 or int(option) == 4 or int(option) == 5:
            return int(option)
        else:
            print("Please enter either 1, 2, 3, 4 or 5.")


def show_clinician_options():
    while True:
        print('''What do you want to do next?
> Press [1] to view your slots.
> Press [2] to create slot.
> Press [3] to delete a slot.
> Press [4] go back to main menu.
> Press [5] to turn off program.\n''')
        option = input("Enter your option here: ")
        if int(option) == 1 or int(option) == 2 or int(option) == 3 or int(option) == 4 or int(option) == 5:
            return int(option)
        else:
            print("Please enter either 1, 2, 3, 4 or 5.")
