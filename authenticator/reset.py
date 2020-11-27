# def reset_pass():
#     username = input("Please enter your username: ")
#     username = encrypter.encrypt_username(username)
#     with open("users.txt", 'r') as usernames:    
#         if username in usernames.read():
#             return username


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
    username = input("Please enter your username: ")
    if len(username) > 0:
        with open("authenticator/users.txt", 'r') as usernames:    
            if username in usernames.read():
                with open("authenticator/users.txt", "r") as file:
                    lines = file.readlines()
                with open("authenticator/users.txt", "w") as file:
                    for line in lines:
                        line = line.split(",")
                        if username == line[0]:
                            pass
                        else :
                            file.write("" + line[0] + "," + line[1] + "")
    else :
        return reset_main()
            
reset_main()