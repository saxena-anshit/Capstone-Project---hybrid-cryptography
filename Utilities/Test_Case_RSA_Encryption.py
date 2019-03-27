from RSA_Encryption import RSA_Encryption, generate_keys, encrypt_data, decrypt_data

import unittest
import math

class TestStringMethods(unittest.TestCase): 
    
    def setUp(self): 
        pass
    

    def is_prime(self, number):
        if number == 2:
            return True

        if not number & 1:
            return False

        return pow(2, number - 1, number) == 1


    def test_generate_prime_number(self):		 
        self.assertTrue(self.is_prime(RSA_Encryption().generate_prime_number()))


    def test_modular_mult_inverse(self):		 
        self.assertEqual(RSA_Encryption().modular_mult_inverse(9, 26), 3)


    def test_encrypt_string(self): 
        self.assertEqual(RSA_Encryption().encrypt_string("hello", 47, 143), "91 95 114 114 67")


    def test_decrypt_string(self): 
        self.assertEqual(RSA_Encryption().decrypt_string("91 95 114 114 67", 23, 143), "hello")


if __name__ == '__main__': 
    unittest.main() 
