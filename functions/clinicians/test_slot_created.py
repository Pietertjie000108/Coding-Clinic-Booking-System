import sys, os, inspect
from io import StringIO


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


import unittest

#from test_base import captured_io
import calender_api
import date_format as df
import datetime
import create_clinician_slot
#import auth_interface

service = calender_api.create_auth_service()

# colors = service.colors().get().execute()
d_and_t = df.get_add_to_calender_input("2020-12-09", "11:45")
# now = datetime.datetime.now()
start2 = df.convert_to_RFC_datetime(d_and_t[0], d_and_t[1], d_and_t[2], d_and_t[3][0]-2, d_and_t[3][1])
end = df.convert_to_RFC_datetime(d_and_t[0], d_and_t[1], d_and_t[2], d_and_t[4][0]-2, d_and_t[4][1])


# if auth_interface.check_if_credentials_have_expired():
#         return
class MyTestCase(unittest.TestCase):

    def test_slots_overlap(self):
        global service, start2, end
        
        username = "nmeintje"
        
        a = create_clinician_slot.check_if_slots_overlap(start2, end, service, username)
        self.assertEqual(a,True)
        d_and_t = df.get_add_to_calender_input("2020-12-09", "11:00")
        start2 = df.convert_to_RFC_datetime(d_and_t[0], d_and_t[1], d_and_t[2], d_and_t[3][0]-2, d_and_t[3][1])
        end = df.convert_to_RFC_datetime(d_and_t[0], d_and_t[1], d_and_t[2], d_and_t[4][0]-2, d_and_t[4][1])
        a = create_clinician_slot.check_if_slots_overlap(start2, end, service, username)
        self.assertEqual(a,False)
        
    """
    def test_add_to_calendar(self):
        overlaps = False
        with captured_io(StringIO("2020-12-09 11:00")) as (out, err):
            output = out.getvalue().strip()
        self.assertEqual(output,)
    """

if __name__=="__main__":
    unittest.main()