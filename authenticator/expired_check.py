import os, datetime, re

def is_program_expired():
    # Query date of first lauch in given file
    if os.path.exists("username_file"):
        with open("username_file", 'r') as file:
            lines = file.read()
            for line in lines:
                if  re.search('[0-9]',line) is not None:
                    start_date = datetime.datetime.strptime(line, "%H")
                    # start_date = datetime.datetime.strptime(line, "%Y_%m_%d_%H_%M_%S")
                    # Check if current time is greater than time limit
                    expire_date = start_date + datetime.timedelta(hours=1)
                    if datetime.datetime.now() > expire_date:
                        file.close()
                        os.remove("username_file")
                        print("Your login has expired.")
                        return True
                    else :
                        return False
                else :
                    continue


is_program_expired()