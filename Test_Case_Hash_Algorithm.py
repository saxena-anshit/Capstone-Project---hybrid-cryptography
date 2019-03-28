#Test case for Hash algorithm

from Utilities.Hash_Algorithm import hash_function

import unittest
import hashlib


class TestStringMethods(unittest.TestCase): 
    
    def setUp(self): 
        pass

    def test_module_1_hash_function(self):
        self.assertEqual(hash_function("hello"), hashlib.sha256("hello".encode('utf-8')).hexdigest())

    def test_module_2_hash_function(self):
        self.assertEqual(hash_function("AbdeManaaf Ghadiali"), hashlib.sha256("AbdeManaaf Ghadiali".encode('utf-8')).hexdigest())

    def test_module_3_hash_function(self):
        self.assertEqual(hash_function("1234567890"), hashlib.sha256("1234567890".encode('utf-8')).hexdigest())

    def test_module_4_hash_function(self):
        self.assertEqual(hash_function("Abde1998Manaaf"), hashlib.sha256("Abde1998Manaaf".encode('utf-8')).hexdigest())

    def test_module_5_hash_function(self):
        self.assertEqual(hash_function("Abde@1123!@"), hashlib.sha256("Abde@1123!@".encode('utf-8')).hexdigest())

    def test_module_6_hash_function(self):
        self.assertEqual(hash_function("12345!@#$%"), hashlib.sha256("12345!@#$%".encode('utf-8')).hexdigest())

    def test_module_7_hash_function(self):
        self.assertEqual(hash_function("Hello::World"), hashlib.sha256("Hello::World".encode('utf-8')).hexdigest())

    def test_module_8_hash_function(self):
        self.assertEqual(hash_function("Capstone_Project_1234567890_"), hashlib.sha256("Capstone_Project_1234567890_".encode('utf-8')).hexdigest())

    def test_module_9_hash_function(self):
        self.assertEqual(hash_function("Easy_Peasy"), hashlib.sha256("Easy_Peasy".encode('utf-8')).hexdigest())

    def test_module_10_hash_function(self):
        self.assertEqual(hash_function("45678Linux666"), hashlib.sha256("45678Linux666".encode('utf-8')).hexdigest())


if __name__ == '__main__': 
    unittest.main() 
