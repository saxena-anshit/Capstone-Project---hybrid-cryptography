import hashlib

def hash_function(plain_text):
    return hashlib.sha256(plain_text.encode('utf-8')).hexdigest()