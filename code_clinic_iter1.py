import json
import os
import random

valid_users = ['student', 'volunteer']
valid_check = ['1', '2', '3', '4', '5']


def help_commands():
    print("These are the commands: \n   1) Book: you can book a coding clinic.\n   2) Create: You can create a coding clinc.\n   3) Delete: You can delete open slots. \n   4) Events: You can vieew your events for the next 7 days.")


def user_name():
    name = input("what is your username? ")
    return name


def user_check():
    user = ''
    while user not in valid_users:
        user = input("Are you a student or volunteer? ")
    return user


def random_id():
    id_rand = random.randint(0,999999999)
    return str(id_rand)


def event_create(name):
    print("Insert event creation sequence here: ")
    event_id = random_id()
    loc = input("Where are you? WTC or W17: ")
    summary = input("What topics can you assist with?")

    with open('data_files/'+event_id+'.json', 'w+') as outfile:
       
        test = {'Organiser: ': name,
            'Event: ': event_id,
            'Title' : 'Code Clinic',
            'Desc': summary,
            'From: ': loc,
            'Users': name}

        json.dump(test, outfile, sort_keys=True, indent=4)


def command_handler(command, name, user):
    if command == "student":
        event = input("What session would you like to book? ")
        print(f""+name+ ", you have booked event: "+ event + ".")

    elif command == "delete":
        event_id = input("What event would you like to delete? ")
        os.remove(f"data_files/" + event_id + ".json")
        print(f"Event: " + str(event_id) + " was deleted successfully by " + str(user) + ": " + str(name) + ".")

    elif command == 'events':
        print("These are your events for the next 7 days")

    elif command == 'help':
        help_commands()

    elif command == 'create':
        event_create(name)
    

def user_input(user):
    check = ''
    while check not in valid_check:
        check = input("Code Clinic Tool:\n 1) Book a slot: \n 2) Create a slot: \n 3) delete a slot: \n 4) Display events: \n 5) Help function \n Pick a number: ")
        if check == '1' and user.lower()  == 'student':
            return 'student'
        elif check == '2' and user.lower() == 'volunteer':
            return 'create'
        elif check == '3' and user.lower()  == 'volunteer':
            return 'delete'
        elif check == '4':
            return 'events'
        elif check == '5':
            return 'help'


def sequence():
    name = user_name()
    user = user_check()
    command = user_input(user)
    command_handler(command, name, user)


if __name__ == '__main__':
    sequence()
