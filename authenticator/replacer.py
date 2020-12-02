import getch
def getpass(prompt):
    """Replacement for getpass.getpass() which prints asterisks for each character typed"""
    print(prompt, end='', flush=True)
    output = ''
    while True:
        char = getch.getch()
        if char == '\n':
            print('')
            break
        else:
            output += char
            print('*', end='', flush=True)
    return output