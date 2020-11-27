# def encrypt_username(username):
#     encrypt_user = ''
#     for letter in username:
#         if letter == " ":
#             encrypt_user += " "
#         else :
#             encrypt_user += chr(ord(letter) + 5)
        
#     return encrypt_user

def encrypt_password(password):
    encrypt_pass = ''
    for letter in password:
        if letter == " ":
            encrypt_pass += " "
        else :
            encrypt_pass += chr(ord(letter) + 5)
        
    return encrypt_pass