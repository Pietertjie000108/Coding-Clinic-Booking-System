import encrypter
import re


def write_new_user():
    """
    [writing user data to a txt file, encrypting it before it saves.]
    """
    with open("users.txt", "a+") as file_ob:
        file_ob.seek(0)
        data = file_ob.read(100)
        user = ''
        pswd = ''
        if len(data) > 0:
            username,password = user_and_pass()
            user = encrypter.encrypt_username(username)
            pswd = encrypter.encrypt_password(password)
            if robot_test() == False:
                file_ob.write("\n"+user + "," + pswd + "")
            else: 
                print("It's a trap!!!")

                

def new_username():
    """
    [getting input from the user, seeing if that data is saved 
    if it is prompts the user to enter another password,
    otherwise it encrypts it and saves it.]

    Returns:
        [string]: [returns the user input.]
    """
    username = input("Please enter your username: ")
    user1 = encrypter.encrypt_username(username)
    with open("users.txt", 'r') as usernames:    
        if user1 in usernames.read():
            usernames.close()
            print("That user already exists.")
            return new_username()
        else:
            usernames.close()
            return username


def password():
    """
    [calling the validation function and saving its value as the users password.
    having the user re-enter password.]

    Returns:
        [type]: [description]
    """
    password1 = validate()
    password_check = ''
    while password1 != password_check:
        password_check = input("Please re-enter password: ")
    return password1
    

def validate():
    """[a function used to check user input and save a strong password.]

    Returns:
        [string]: [users password]
    """
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
    """[Just a fun little easte egg, seeing if the useer is a robot or not]

    Returns:
        [bool]: [False: if user is human, True if its a robot.]
    """
    valid_answers = ['1', '2', '3']
    answer = input("Are you a robot? \n 1) No. \n 2) Yes. \n 3) I really need to focos on other things XD!!!\n")
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

write_new_user()