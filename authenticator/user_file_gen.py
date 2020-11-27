import datetime
import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

def create_username_file(username): 
    start_date = datetime.datetime.now()
    with open("username_file", 'w') as file:
        file.write(start_date.strftime("%Y_%m_%d_%H_%M_%S\n"))
        file.write(username)
        file.close()

            #make into own function to be called. bool return values