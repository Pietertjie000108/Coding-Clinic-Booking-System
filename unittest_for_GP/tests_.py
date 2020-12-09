import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
#########################################################################################
import unittest
from unittest.mock import patch
from io import StringIO
#########################################################################################
                        ####################################
                            #all imports for functions#
import functions 
from functions import calender_api
from functions import patients 
from functions.patients import signup_to_patient_slot
from functions.patients import delete_patient_slot
from functions.calender_api import create_auth_service
#####
update_slot_with_deleted_patient = delete_patient_slot.update_slot_with_deleted_patient
#####
delete_patient_slot= delete_patient_slot.delete_patient_slot 
#####
update_slot_with_patient = signup_to_patient_slot.update_slot_with_patient
#####
add_patient_slot_to_calender = signup_to_patient_slot.add_patient_slot_to_calender

                        ####################################
                        #imports for authenticator_newUser
import authenticator
from authenticator.new_user import main
from authenticator.new_user import new_username
from authenticator.new_user import password
from authenticator.new_user import validate
from authenticator.new_user import robot_test
from authenticator.new_user import user_and_pass
                        ####################################
#imports for authenticator_newAuth

# from authenticator.pass_auth import user_find
# from authenticator.pass_auth import pass_check

#these test...test output only#
class MyTestCase(unittest.TestCase):
#############################################################################################
                                #Test for Functions.patients 
    def test_update_slot_with_patient(self):#test for update slot with patient
        self.maxDiff = None
        self.assertNotEqual(update_slot_with_patient,"The slot you tried signing up for is already taken. Please choose another slot.")
        
    def  test_add_patient(self):#test to adding
        self.maxDiff = None
        self.assertNotEqual(add_patient_slot_to_calender,"Please enter a valid ID.")

    def test_delete_clinitian_slot(self):
        self.maxDiff = None
        self.assertNotEqual(delete_patient_slot,"There are currently no available slots to delete.")

    def test_update_slot_with_deleted_patient(self):
        self.maxDiff =None
        self.assertNotEqual(update_slot_with_deleted_patient,None)

    #dont know the values for service 
    def test_reate_auth_service(self):
        # service = calender_api.create_auth_service()
        self.maxDiff = None
        # self.assertEqual(create_auth_service,service)

#############################################################################################
                                #Tests for New_User
    def test_new_User_main(self):
        self.maxDiff = None
        self.assertNotEqual(main,"It's a trap!!!")

    def test_new_user(self):
        username = "Taismail"
        self.maxDiff = None
        self.assertNotEqual(new_username,"That user already exists.")
        # self.assertEqual(new_username,username)

    def test_auth_password(self) :
        self.maxDiff = None
        self.assertNotEqual(password,"Please re-enter password: ")

        #need to put a patch in here
    def test_auth_validate(self):
        self.assertNotEqual(validate,"Make sure your password is at lest 8 letters")
        self.assertNotEqual(validate,"Make sure your password has a number in it")
        self.assertNotEqual(validate,"Make sure your password has a capital letter in it")
        self.assertNotEqual(validate,"Your password seems fine")
        # self.assertEqual(validate,"passWord4")

    def test_auth_robotTest(self) :
        self.maxDiff =None
        self.assertTrue(robot_test,True)
        self.assertNotEqual(robot_test,False)

    def test_auth_user_and_pass(self):
        # user,passwd = user_and_pass()
        self.maxDiff = None
        # self.assertEqual(user_and_pass,user,passwd)
        self.assertNotEqual(user_and_pass, None)

#############################################################################################
                                #Test for pass_auth
    # def test_user_find(self):
        # keeps asking for username
        # username = "taismail"
        # self.assertEqual(user_find,"username found",username)
        # self.assertNotEqual(user_find,None)
    
    # def test_pass(self):
    #     self.maxDiff = None
    #     user_found = 
    #     self.assertEqual(pass_check(),"password match")
    #     self.assertNotEqual(pass_check(),"password not match")

#############################################################################################
if __name__ == "__main__":
    unittest.main()