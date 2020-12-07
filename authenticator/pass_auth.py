import sys, os, inspect
import csv
import encrypter
import user_file_gen as gen
# import replacer
import stdiomask



currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


def main():
    """
    Main login system
    """
    with open("authenticator/users.txt","r") as file:
        file_reader = csv.reader(file)
        user_find(file_reader)
        file.close()

def user_find(file):
    """
    check through the users file for the username inputted.

    file is the file we are using to store user data.
    """
    username1 = input("Enter your username: ")
    username = username1.lower()
    for row in file:
        if row[0] == username:
            print("username found", username)
            user_found = [row[0],row[1]]
            pass_check(user_found)
            gen.create_username_file(username)
            break
        else:
            continue
            #print("not found")

def pass_check(user_found):
    """
    checking users input against saved data

    user_found is the row the function is working with.
    """
    password = ''
    while password != user_found[1]:
        password = stdiomask.getpass(prompt="Please enter your password: ", mask='*')
        pass1 = encrypter.encrypt_password(password)
        if user_found[1] == pass1:
            return "password match"
        else:
            print("password not match")

main()