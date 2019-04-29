from .utilities.rsa_encryption import decrypt_data
from .utilities.hash_algorithm import hash_function

import base64
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_from_en_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()
    

def read_keys(key_file):
    with open(key_file, 'r') as file:
        key_str = base64.b64decode(file.readlines()[1].encode('utf-8')).decode('utf-8')
        return str(key_str).split()
    
    
def write_to_de_file(decrypted_text, name, ext):
    decrypted_file_path = os.path.join(BASE_DIR, 'media/' + name + '.' + ext)

    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_text.encode("utf-8"))
        
    return True
    
    
def xor_with_pad(bin_str, one_time_password):
    encrypted_file = ''
    
    for byte in bin_str.split(' '):
        encrypted_file += str(bin(int(byte, 2) ^ int(one_time_password, 2))[2:]) + " "
        
    return encrypted_file


def bin_to_chr(bin_str):    
    return ''.join(chr(int(i, 2)) for i in bin_str.split(' '))


def decrypt(file_name, key_file, name, ext):
    prime_pxq, d, one_time_password = int(read_keys(key_file)[0]), int(read_keys(key_file)[1]), read_keys(key_file)[2]
    
    encrypted_file = str(read_from_en_file(file_name)).strip()
    bin_str = str(xor_with_pad(encrypted_file, one_time_password)).strip()
    
    temp_var = bin_to_chr(bin_str).split(' ')
        
    encrypted_text = ' '.join([temp_var[item] for item in range(len(temp_var) - 1)])
        
    decrypted_text = decrypt_data(encrypted_text, d, prime_pxq)
        
    if hash_function(decrypted_text) == temp_var[-1]:
        try:
            write_to_de_file(decrypted_text, name, ext)
            return True
        
        except:
            return False
    else:
        print("Hash does not match!!")

    return False


def read_file_dec(enc_file_path, public_key_path, file_name):
    name, ext, temp = file_name.split(".")
    decrypt(enc_file_path, public_key_path, name, ext)
