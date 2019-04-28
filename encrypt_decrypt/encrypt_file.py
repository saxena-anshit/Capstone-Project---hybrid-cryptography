from .utilities.rsa_encryption import generate_keys, encrypt_data
from .utilities.hash_algorithm import hash_function

from Crypto.Util import number

import base64
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def write_to_en_file(encrypted_file, name, ext):
    encrypted_file_path = os.path.join(BASE_DIR, 'media/encrypted_files/' + name + '.' + ext)

    with open(encrypted_file_path, 'w') as file:
        file.write(encrypted_file)
        
    return True


def save_keys(keys, file_name):
    private_key_path = os.path.join(
        BASE_DIR, 'media/private_keys/' + 'private_key_' + file_name + '.txt')

    with open(private_key_path, 'w') as file:
        
        concat_keys = str(keys[0]) + ' ' + str(keys[1]) + ' ' + str(keys[3])
        base64_key = base64.b64encode(concat_keys.encode('utf-8'))
        
        key_file = '-----BEGIN OF RSA PRIVATE KEY-----\n' + str(base64_key.decode('utf-8')) + '\n-----END OF RSA PRIVATE KEY-----'
        file.write(key_file)
        
    public_key_path = os.path.join(
        BASE_DIR, 'media/public_keys/' + 'public_key_' + file_name + '.txt')

    with open(public_key_path, 'w') as file:
        concat_keys = str(keys[0]) + ' ' + str(keys[2]) + ' ' + str(keys[3])
        base64_key = base64.b64encode(concat_keys.encode('utf-8'))
        
        key_file = '-----BEGIN OF RSA PUBLIC KEY-----\n' + str(base64_key.decode('utf-8')) + '\n-----END OF RSA PUBLIC KEY-----'
        file.write(key_file)

    return True


def get_bin_str(encrypted_text):    
    return ' '.join(format(ord(x), 'b') for x in encrypted_text)
    

def xor_with_pad(bin_str, one_time_password):    
    encrypted_file = ''
    
    for byte in bin_str.split(' '):
        encrypted_file += str(bin(int(byte, 2) ^ int(one_time_password, 2))[2:]) + " "
        
    return encrypted_file


def generate_pass_keys():
    prime_pxq, e, d = generate_keys()
    one_time_password = bin(number.getPrime(16))[2:]
    
    return prime_pxq, d, e, one_time_password
    

def encrypt(plain_text, file_name):    
    keys = list(generate_pass_keys())
    name, ext = file_name.split(".")

    save_keys(keys, name)
    
    prime_pxq, e, one_time_password = keys[0], keys[1], keys[3]

    encrypted_text = encrypt_data(plain_text, e, prime_pxq)    
        
    bin_str = get_bin_str(encrypted_text + ' ' + hash_function(plain_text))    
    encrypted_file = xor_with_pad(bin_str, one_time_password)
        
    try:
        if name == None and ext == None:
            name = 'text_message'
            ext = 'txt'
            
        write_to_en_file(encrypted_file, name, ext)
    except:
        return False
    
    return True

def read_file(file_path, file_name):
    plain_text = open(file_path, 'rb').read().decode("utf-8")
    encrypt(plain_text, file_name)