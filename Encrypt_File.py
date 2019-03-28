from Utilities.RSA_Encryption import generate_keys, encrypt_data
from Utilities.Hash_Algorithm import hash_function
from Utilities.One_Time_Pad import one_time_pad_password


def write_to_en_file(encrypted_file, name, ext):
    with open(name + '.en.' + ext, 'w') as file:
        file.write(encrypted_file)
        
    return True


def save_keys(keys):
    with open('private_key.txt', 'w') as file:
        key_file = str(keys[0]) + ' ' + str(keys[1]) + ' ' + str(keys[3])
        file.write(key_file)
        
    with open('public_key.txt', 'w') as file:
        key_file = str(keys[0]) + ' ' + str(keys[2]) + ' ' + str(keys[3])
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
    one_time_password = one_time_pad_password()
    
    return prime_pxq, e, d, one_time_password
    

def encrypt(plain_text, name=None, ext=None):    
    keys = list(generate_pass_keys())
    save_keys(keys)
    
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
    
    
if __name__ == '__main__':
    file_name = input("Enter the file name to encrypt: ")
    name, ext = file_name.split(".")
        
    plain_text = open(file_name, 'rb').read().decode("utf-8")
        
    success = encrypt(plain_text, name, ext)
    
    if success:
        print("\nFile Encryption Successful::Saved to Database")
