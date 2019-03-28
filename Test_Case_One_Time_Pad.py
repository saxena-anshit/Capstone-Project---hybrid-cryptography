# This is a one time pad test case
from Utilities.One_Time_Pad import one_time_pad_password

import unittest


class TestStringMethods(unittest.TestCase):
    
    def setUp(self): 
        pass

    def test_one_time_pad_password(self): 
        self.assertEqual(len(one_time_pad_password()), 16)


if __name__ == '__main__': 
    unittest.main() 
