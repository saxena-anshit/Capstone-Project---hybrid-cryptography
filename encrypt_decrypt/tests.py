from django.test import TestCase
from .utilities.rsa_encryption import RSA_Encryption, generate_keys, encrypt_data, decrypt_data
from .utilities.hash_algorithm import hash_function

import hashlib

class RSAEncryptionTestCase(TestCase):

    def setUp(self):
        pass

    def is_prime(self, number):
        if number == 2:
            return True

        if not number & 1:
            return False

        return pow(2, number - 1, number) == 1

    def test_1_generate_prime_number(self):
        self.assertTrue(self.is_prime(RSA_Encryption().generate_prime_number()))

    def test_2_generate_prime_number(self):
        self.assertTrue(self.is_prime(RSA_Encryption().generate_prime_number()))

    def test_3_generate_prime_number(self):
        self.assertTrue(self.is_prime(RSA_Encryption().generate_prime_number()))

    def test_4_generate_prime_number(self):
        self.assertTrue(self.is_prime(RSA_Encryption().generate_prime_number()))

    def test_5_generate_prime_number(self):
        self.assertTrue(self.is_prime(RSA_Encryption().generate_prime_number()))

    def test_1_modular_mult_inverse(self):
        self.assertEqual(RSA_Encryption().modular_mult_inverse(1000619, 1001640), 282539)

    def test_2_modular_mult_inverse(self):
        self.assertEqual(RSA_Encryption().modular_mult_inverse(1000621, 1001640), 351901)

    def test_3_modular_mult_inverse(self):
        self.assertEqual(RSA_Encryption().modular_mult_inverse(1000627, 1001640), 13843)

    def test_4_modular_mult_inverse(self):
        self.assertEqual(RSA_Encryption().modular_mult_inverse(1000631, 1001640), 246191)

    def test_5_modular_mult_inverse(self):
        self.assertEqual(RSA_Encryption().modular_mult_inverse(1000633, 1001640), 594817)

    def test_1_encrypt_string(self):
        self.assertEqual(RSA_Encryption().encrypt_string("hello", 47, 143), "91 95 114 114 67")

    def test_2_encrypt_string(self):
        self.assertEqual(RSA_Encryption().encrypt_string("AbdeManaaf Ghadiali", 47, 143),
                         "65 54 133 95 77 37 11 37 37 97 76 102 91 37 133 118 37 114 118")

    def test_3_encrypt_string(self):
        self.assertEqual(RSA_Encryption().encrypt_string("1234567890", 47, 143), "69 19 116 13 92 98 22 23 73 16")

    def test_4_encrypt_string(self):
        self.assertEqual(RSA_Encryption().encrypt_string("Abde1998Manaaf", 47, 143),
                         "65 54 133 95 69 73 73 23 77 37 11 37 37 97")

    def test_5_encrypt_string(self):
        self.assertEqual(RSA_Encryption().encrypt_string("Abde@1123!@", 47, 143),
                         "65 54 133 95 103 69 69 19 116 132 103")

    def test_6_encrypt_string(self):
        self.assertEqual(RSA_Encryption().encrypt_string("12345!@#$%", 47, 143), "69 19 116 13 92 132 103 29 108 71")

    def test_7_encrypt_string(self):
        self.assertEqual(RSA_Encryption().encrypt_string("Hello::World", 47, 143),
                         "41 95 114 114 67 141 141 120 67 82 114 133")

    def test_8_encrypt_string(self):
        self.assertEqual(RSA_Encryption().encrypt_string("Capstone_Project_1234567890_", 47, 143),
                         "111 37 18 58 129 67 11 95 127 20 82 67 72 95 44 129 127 69 19 116 13 92 98 22 23 73 16 127")

    def test_9_encrypt_string(self):
        self.assertEqual(RSA_Encryption().encrypt_string("Easy_Peasy", 47, 143), "75 37 58 88 127 20 95 37 58 88")

    def test_10_encrypt_string(self):
        self.assertEqual(RSA_Encryption().encrypt_string("45678Linux666", 47, 143),
                         "13 92 98 22 23 32 118 11 39 87 98 98 98")

    def test_1_decrypt_string(self):
        self.assertEqual(RSA_Encryption().decrypt_string("91 95 114 114 67", 23, 143), "hello")

    def test_2_decrypt_string(self):
        self.assertEqual(RSA_Encryption().decrypt_string(
            "65 54 133 95 77 37 11 37 37 97 76 102 91 37 133 118 37 114 118", 23, 143), "AbdeManaaf Ghadiali")

    def test_3_decrypt_string(self):
        self.assertEqual(RSA_Encryption().decrypt_string("69 19 116 13 92 98 22 23 73 16", 23, 143), "1234567890")

    def test_4_decrypt_string(self):
        self.assertEqual(RSA_Encryption().decrypt_string("65 54 133 95 69 73 73 23 77 37 11 37 37 97", 23, 143),
                         "Abde1998Manaaf")

    def test_5_decrypt_string(self):
        self.assertEqual(RSA_Encryption().decrypt_string("65 54 133 95 103 69 69 19 116 132 103", 23, 143),
                         "Abde@1123!@")

    def test_6_decrypt_string(self):
        self.assertEqual(RSA_Encryption().decrypt_string("69 19 116 13 92 132 103 29 108 71", 23, 143), "12345!@#$%")

    def test_7_decrypt_string(self):
        self.assertEqual(RSA_Encryption().decrypt_string("41 95 114 114 67 141 141 120 67 82 114 133", 23, 143),
                         "Hello::World")

    def test_8_decrypt_string(self):
        self.assertEqual(RSA_Encryption().decrypt_string(
            "111 37 18 58 129 67 11 95 127 20 82 67 72 95 44 129 127 69 19 116 13 92 98 22 23 73 16 127", 23, 143),
            "Capstone_Project_1234567890_")

    def test_9_decrypt_string(self):
        self.assertEqual(RSA_Encryption().decrypt_string("75 37 58 88 127 20 95 37 58 88", 23, 143), "Easy_Peasy")

    def test_10_decrypt_string(self):
        self.assertEqual(RSA_Encryption().decrypt_string("13 92 98 22 23 32 118 11 39 87 98 98 98", 23, 143),
                         "45678Linux666")

    def test_1_modular_hash_function(self):		 
        self.assertEqual(hash_function("hello"), hashlib.sha256("hello".encode('utf-8')).hexdigest())

    def test_2_modular_hash_function(self):		 
        self.assertEqual(hash_function("Abdemanaaf"), hashlib.sha256("Abdemanaaf".encode('utf-8')).hexdigest())

    def test_3_modular_hash_function(self):		 
        self.assertEqual(hash_function("123456789"), hashlib.sha256("123456789".encode('utf-8')).hexdigest())

    def test_4_modular_hash_function(self):		 
        self.assertEqual(hash_function("Abde@1998"), hashlib.sha256("Abde@1998".encode('utf-8')).hexdigest())

    def test_5_modular_hash_function(self):		 
        self.assertEqual(hash_function("1234@#$,...hello"), hashlib.sha256("1234@#$,...hello".encode('utf-8')).hexdigest())
