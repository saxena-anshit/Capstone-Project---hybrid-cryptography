from Crypto.Util import number
from math import gcd
from random import choice


class RSA_Encryption:
    
    def __init__(self):
        self.PRIME_NUMBER_BITS = 128
        

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
            if gcd(phi, num) == 1 and self.modular_mult_inverse(num, phi) != None:
                list_of_co_primes.append(num)
        
        for num in list_of_co_primes:
            if num == self.modular_mult_inverse(num, phi):
                list_of_co_primes.remove(num)
        
        return list_of_co_primes


    def encrypt_string(self, plain_text, e, prime_pxq):
        return ' '.join([str(pow(ord(x), e, prime_pxq)) for x in list(plain_text)])
    

    def decrypt_string(self, encrypted_text, d, prime_pxq):
        return ''.join([chr(pow(int(x), d, prime_pxq)) for x in encrypted_text.strip().split(' ')])


def generate_keys():
    rsa_encryption = RSA_Encryption()

    prime_p = rsa_encryption.generate_prime_number()
    prime_q = rsa_encryption.generate_prime_number()
        
    while prime_p == prime_q:
        prime_q = rsa_encryption.generate_prime_number()
    
    prime_pxq = prime_p * prime_q
    phi = (prime_p - 1) * (prime_q - 1)
    
    e = choice(list(reversed(rsa_encryption.co_primes(phi))))
    d = rsa_encryption.modular_mult_inverse(e, phi)

    return prime_pxq, e, d
        

def encrypt_data(plain_text, e, prime_pxq):
    return RSA_Encryption().encrypt_string(plain_text, e, prime_pxq)


def decrypt_data(encrypted_text, d, prime_pxq):
    return RSA_Encryption().decrypt_string(encrypted_text, d, prime_pxq)