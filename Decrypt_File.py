from Utilities.RSA_Encryption import decrypt_data
from Utilities.Hash_Algorithm import hash_function


def read_from_en_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()
    

def read_keys(key_file):
    with open(key_file, 'r') as file:
        return str(file.read()).split()
    
    
def write_to_de_file(decrypted_text, name, ext):
    with open(name + '.de.' + ext, 'wb') as file:
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


if __name__ == '__main__':
    
    file_name = input("Enter the file name to decrypt: ")
    key_file = input("Enter the name of the key's file: ")
    name, temp, ext = file_name.split(".")
        
    success = decrypt(file_name, key_file, name, ext)
    
    if success:
        print("\nFile Decryption Successful")
