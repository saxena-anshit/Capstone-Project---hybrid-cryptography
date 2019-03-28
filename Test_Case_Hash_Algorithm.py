from Utilities.Hash_Algorithm import hash_function

import unittest
import hashlib


class TestStringMethods(unittest.TestCase): 
    
    def setUp(self): 
        pass


    def test_modular_hash_function(self):
        self.assertEqual(hash_function("hello"), hashlib.sha256("hello".encode('utf-8')).hexdigest())


if __name__ == '__main__': 
    unittest.main() 
