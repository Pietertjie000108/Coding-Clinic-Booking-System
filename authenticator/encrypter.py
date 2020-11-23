def encrypt_username(username):
    """[encrypting the username so that it cant be seen normally]

    Args:
        username ([string]): [the input recieved is the username]

    Returns:
        [string]: [an encrypted username where each letter has had their value changed]
    """
    encrypt_user = ''
    for letter in username:
        if letter == " ":
            encrypt_user += " "
        else :
            encrypt_user += chr(ord(letter) + 5)
        
    return encrypt_user

def encrypt_password(password):
    """[encrypting the password so that it cant be seen normally]

    Args:
        username ([string]): [the input recieved is the password]

    Returns:
        [string]: [an encrypted password where each letter has had their value changed]
    """
    encrypt_pass = ''
    for letter in password:
        if letter == " ":
            encrypt_pass += " "
        else :
            encrypt_pass += chr(ord(letter) + 5)
        
    return encrypt_pass