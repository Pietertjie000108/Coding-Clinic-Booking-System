import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import encrypter
import re


def main():
    with open("authenticator/users.txt", "a+") as file_ob:
        file_ob.seek(0)
        data = file_ob.read(100)
        user = ''
        pswd = ''
        if len(data) > 0:
            username,password = user_and_pass()
            user = username
            pswd = encrypter.encrypt_password(password)
            if robot_test() == False:
                file_ob.write("\n"+user + "," + pswd + "")
            else: 
                print("It's a trap!!!")

                

def new_username():
    username = input("Please enter your username: ")
    with open("authenticator/users.txt", 'r') as usernames:
        if username in usernames.read():
            usernames.close()
            print("That user already exists.")
            return new_username()
        else:
            usernames.close()
            return username


def password():
    password1 = validate()
    password_check = ''
    while password1 != password_check:
        password_check = input("Please re-enter password: ")
    return password1
    

def validate():
    while True:
        password = input("Please enter a password longer than 8 characters: ")
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a capital letter in it")
        else:
            print("Your password seems fine")
            return password


def robot_test():
    valid_answers = ['1', '2']
    answer = input("Are you a robot? \n 1) No. \n 2) Yes. \n")
    while answer in valid_answers:
        if answer == '1':
            return False
        else :
            return True
    else :
        return True


def user_and_pass():
    user = new_username()
    passwd = password()
    return user,passwd

main()