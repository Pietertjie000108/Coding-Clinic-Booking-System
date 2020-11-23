def decrypt_username(username):
    """[decrypting the username so that it can be read normally by the program]

    Args:
        username ([string]): [the encrypted username to be decrypted]

    Returns:
        [string]: [the decrypted username]
    """
    decrypt_user = ''
    for letter in username:
        if letter == " ":
            decrypt_user += " "
        else :
            decrypt_user += chr(ord(letter) - 5)
        
    return decrypt_user

def decrypt_password(password):
    """[decrypting the password so that it can be read normally by the program]

    Args:
        username ([string]): [the encrypted password to be decrypted]

    Returns:
        [string]: [the decrypted password]
    """
    decrypt_pass = ''
    for letter in password:
        if letter == " ":
            decrypt_pass += " "
        else :
            decrypt_pass += chr(ord(letter) - 5)
        
    return decrypt_pass