import encrypter
import decrypter

# def reset_pass():
#     username = input("Please enter your username: ")
#     user1 = encrypter.encrypt_username(username)
#     with open("users.txt", 'r') as usernames:    
#         if user1 in usernames.read():
#             return user1


# def redo_user_list(username):
#     with open("users.txt", "r") as file:
#         lines = file.readlines()
#     with open("users.txt", "w") as file:
#         for line in lines:
#             if username in line:
#                 pass
#             else :
#                 file.write(line)

# def main_reset():
#     username = reset_pass()
#     redo_user_list(username)


def reset_main():
    """[A function used to reset a user,
    takes input of user to reset, finds it in the file
    if it is found it is it gets passed
    oother lines get writen to the file.]

    Returns:
        [function]: [if the length of user input was 0, we recall the function.]
    """
    username = input("Please enter your username: ")
    if len(username) > 0:
        user1 = encrypter.encrypt_username(username)
        # dec_user1 = decrypter.decrypt_username(user1)
        with open("users.txt", 'r') as usernames:    
            if user1 in usernames.read():
                with open("users.txt", "r") as file:
                    lines = file.readlines()
                with open("users.txt", "w") as file:
                    for line in lines:
                        line = line.split(",")
                        if user1 == line[0]:
                            pass
                        else :
                            file.write("" + line[0] + "," + line[1] + "")
    else :
        return reset_main()
            
reset_main()