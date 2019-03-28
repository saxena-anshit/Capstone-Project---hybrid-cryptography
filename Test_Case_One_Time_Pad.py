from Utilities.One_Time_Pad import one_time_pad_password

import unittest
import math

class TestStringMethods(unittest.TestCase): 
    
    def setUp(self): 
        pass

    def test_one_time_pad_password(self): 
        self.assertEqual(len(one_time_pad_password()), 256)


if __name__ == '__main__': 
    unittest.main() 
