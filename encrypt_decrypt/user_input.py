from Encrypt_File import encrypt
from Decrypt_File import decrypt

import os
import time


def encrypt_decrypt():
    print("\nChoose any one of the following: ")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Delete Files from Server")
    print("4. Exit")
    
    try:
        user_input = int(input(">>> "))
    except ValueError:
        return -1
    
    if user_input in [1, 2, 3, 4]:
        return user_input
    else:
        return -1


def encryption_select():
    print("\nPlease select one of the following options for type of message: ")
    print("1. Text Message")
    print("2. File Application")
    print("3. Go Back")
    
    try:
        user_input = int(input(">>> "))
    except ValueError:
        return -1
    
    if user_input in [1, 2, 3]:
        return user_input
    else:
        return -1


def decryption_select():
    file_name = input("Enter the file name to decrypt: ")
    key_file = input("Enter the name of the key's file: ")
    name, temp, ext = file_name.split(".")
    
    time_start = time.time()
    
    if decrypt(file_name, key_file, name, ext):
        print("\nFile Decryption Successful")
    
    time_end = time.time()
    print("\nDecryption time:: " + str(time_end - time_start))
        
    return True


def text_message_select():
    
    if encrypt(input("Enter a message to encrypt: ")):
        print("\nMessage Encryption Successful::Saved to Database")
        
    return True
        

def file_application_select():
    file_name = input("Enter the file name to encrypt: ")
    name, ext = file_name.split(".")
        
    plain_text = open(file_name, 'rb').read().decode("utf-8")
    
    time_start = time.time()
    
    if encrypt(plain_text, name, ext):
        print("\nFile Encryption Successful::Saved to Database")
    
    time_end = time.time()
    print("\nEncryption time:: " + str(time_end - time_start))
        
    return True


def Main():
    
    en_de = encrypt_decrypt()
    
    while en_de != 4:
        if en_de == 1:
            user_input = encryption_select()
            
            if user_input == 1:
                text_message_select()
                en_de = encrypt_decrypt()
                continue
            
            elif user_input == 2:
                file_application_select()
                en_de = encrypt_decrypt()
                continue
            
            elif user_input == 3:
                en_de = encrypt_decrypt()
                continue
            
            elif user_input == -1:
                print("\nInvalid Input, Please try again!")
                en_de = encrypt_decrypt()
                continue
            
        elif en_de == 2:
            decryption_select()
            en_de = encrypt_decrypt()
            continue
        
        elif en_de == 3:
            print("\nAre you sure you want to delete files from the server?")
            print("Yes / No")
            
            ans = input(">>> ")
            
            if ans.lower() == 'yes' or ans.lower() == 'y':
                try:
                    os.remove("private_key.txt")
                    os.remove("public_key.txt")
                    os.remove("test_file.en.txt")
                    os.remove("test_file.de.txt")
                    en_de = encrypt_decrypt()
                    continue
                
                except FileNotFoundError:
                    print("\nNo files found")
                    en_de = encrypt_decrypt()
                    continue
                
            elif ans.lower() == 'no' or ans.lower() == 'n':
                en_de = encrypt_decrypt()
                continue
            
        elif en_de == -1:
            print("\nInvalid Input, Please try again!")
            en_de = encrypt_decrypt()
            continue

    
if __name__ == '__main__':
    Main()
    