import whirlpool 


def encrypt_password(password):

    text = password
    h1 = whirlpool.new(text.encode('utf-8'))
    hashed_output = h1.hexdigest()

        
    return hashed_output