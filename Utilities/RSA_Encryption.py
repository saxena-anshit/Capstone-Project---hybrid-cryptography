from Crypto.Util import number

import math
import random
import time
import sys


class RSA_Encryption:
    
    def __init__(self):
        self.PRIME_NUMBER_BITS = 512
        

    def generate_prime_number(self):
        return number.getPrime(self.PRIME_NUMBER_BITS)


    def modular_mult_inverse(self, num_1, num_2):
        gcd, inv = self.extended_euclid_algorithm(num_1, num_2)
        
        if gcd == 1:
            return inv % num_2
    
    
    def extended_euclid_algorithm(self, num_1, num_2):        
        x0, x1, y0, y1 = 0, 1, 1, 0
        
        while num_1 != 0:
            quotient, num_2, num_1 = num_2 // num_1, num_1, num_2 % num_1
            y0, y1 = y1, y0 - quotient * y1
            x0, x1 = x1, x0 - quotient * x1
            
        return num_2, x0


    def co_primes(self, phi):
        list_of_co_primes = []
            
        for num in range(phi - 1024, phi):
            if math.gcd(phi, num) == 1 and self.modular_mult_inverse(num, phi) != None:
                list_of_co_primes.append(num)
        
        for num in list_of_co_primes:
            if num == self.modular_mult_inverse(num, phi):
                list_of_co_primes.remove(num)
        
        return list_of_co_primes


    '''def encrypt_string(self, plain_text, e, prime_pxq):
        return ' '.join([str(pow(ord(x), e, prime_pxq)) for x in list(plain_text)])'''

    def encrypt_string(self, plain_text, e, prime_pxq):
        encrypted_text = ''

        for x in range(len(plain_text)):
            encrypted_text += str(pow(ord(plain_text[x]), e, prime_pxq)) + ' '

            if x % 100 == 0:
                sys.stdout.write(f"\r{(float(x)/len(plain_text))*100}")
                sys.stdout.flush()

        print()

        return encrypted_text.strip()
    

    '''def decrypt_string(self, encrypted_text, d, prime_pxq):
        return ''.join([chr(pow(int(x), d, prime_pxq)) for x in encrypted_text.strip().split(' ')])'''

    def decrypt_string(self, encrypted_text, d, prime_pxq):
        plain_text = ''
        encrypted_text = encrypted_text.split(' ')

        for x in range(len(encrypted_text)):
            plain_text += chr(pow(int(encrypted_text[x]), d, prime_pxq))

            if x % 100 == 0:
                sys.stdout.write(f"\r{(float(x)/len(encrypted_text))*100}")
                sys.stdout.flush()

        print()

        return plain_text


def generate_keys():
    rsa_encryption = RSA_Encryption()

    prime_p = rsa_encryption.generate_prime_number()
    prime_q = rsa_encryption.generate_prime_number()
        
    while prime_p == prime_q:
        prime_q = rsa_encryption.generate_prime_number()
            
    prime_pxq = prime_p * prime_q
        
    e = random.choice(list(reversed(rsa_encryption.co_primes((prime_p - 1) * (prime_q - 1)))))
    d = rsa_encryption.modular_mult_inverse(e, (prime_p - 1) * (prime_q - 1))
    
    return prime_pxq, e, d
        

def encrypt_data(plain_text, e, prime_pxq):
    return RSA_Encryption().encrypt_string(plain_text, e, prime_pxq)


def decrypt_data(encrypted_text, d, prime_pxq):
    return RSA_Encryption().decrypt_string(encrypted_text, d, prime_pxq)


if __name__ == '__main__':
    
    time_start = time.time()
    prime_pxq, e, d = generate_keys()
    time_end = time.time()
    print("Key Generation time:: " + str(time_end - time_start))
    
    plain_text = input("Enter a message to encrypt: ")
    
    time_start = time.time()
    encrypted_text = encrypt_data(plain_text, e, prime_pxq)
    time_end = time.time()
    print("\nEncrypted message: " + encrypted_text + "\n")
    print("Encryption time:: " + str(time_end - time_start))
    
    time_start = time.time()
    decrypted_text = decrypt_data(encrypted_text, d, prime_pxq)
    time_end = time.time()
owchart    print("\nDecrypted message: " + decrypted_text + "\n")
    print("Decryption time:: " + str(time_end - time_start))

    print(plain_text == decrypted_text)
