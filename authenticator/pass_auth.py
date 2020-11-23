import csv
import decrypter
import encrypter

def main():
    with open("users.txt","r") as file:
        file_reader = csv.reader(file)
        user_find(file_reader)
        file.close()

def user_find(file):
    """[Finding the user in the file they are stored in
    from there looking if the value inputted dequals the value saved.
    also checking the users password aswell]

    Args:
        file ([users.txt]): [file used to save users and their passwords.]
    """
    username = input("Enter your username: ")
    user1 = encrypter.encrypt_username(username)
    for row in file:
        if row[0] == user1:
            username = decrypter.decrypt_username(user1)
            print("username found", username)
            user_found = [row[0],row[1]]
            pass_check(user_found)
            break
        else:
            continue
            #print("not found")

def pass_check(user_found):
    """[A function user to check user input to saved password.]

    Args:
        user_found ([tuple]): [the username and password]

    Returns:
        [string]: [shows if password matches or not.]
    """
    password = ''
    while password != user_found[1]:
        password = input("enter your password: ")
        pass1 = encrypter.encrypt_password(password)
        if user_found[1] == pass1:
            return "password match"
        else:
            print("password not match")

main()