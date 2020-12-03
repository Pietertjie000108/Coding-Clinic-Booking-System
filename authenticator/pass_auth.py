import sys, os, inspect
import csv
import encrypter
import user_file_gen as gen

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


def main():
    '''
    Login after expiration
    '''
    with open("authenticator/users.txt","r") as file:
        file_reader = csv.reader(file)
        user_find(file_reader)
        file.close()

def user_find(file):
    username = input("Enter your username: ")
    for row in file:
        if row[0] == username.lower():
            print("username found", username)
            user_found = [row[0],row[1]]
            pass_check(user_found)
            gen.create_username_file(username)
            break
        else:
            continue
            #print("not found")

def pass_check(user_found):
    password = ''
    while password != user_found[1]:
        password = input("Enter your password: ")
        pass1 = encrypter.encrypt_password(password)
        if user_found[1] == pass1:
            return "password match"
        else:
            print("password not match")

main()