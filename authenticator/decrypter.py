# def decrypt_username(username):
#     decrypt_user = ''
#     for letter in username:
#         if letter == " ":
#             decrypt_user += " "
#         else :
#             decrypt_user += chr(ord(letter) - 5)
        
#     return decrypt_user

def decrypt_password(password):
    decrypt_pass = ''
    for letter in password:
        if letter == " ":
            decrypt_pass += " "
        else :
            decrypt_pass += chr(ord(letter) - 5)
        
    return decrypt_pass