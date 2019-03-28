import hashlib

def hash_function(plain_text):
    return hashlib.sha256(plain_text.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    plain_text = input("Enter a message to encrypt: ")
    print(hash_function(plain_text))