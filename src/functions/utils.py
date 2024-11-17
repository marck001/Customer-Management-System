import bcrypt as by
import random

def encode_hash_function(password):
    
    bytes = password.encode('utf-8') 
    salt = by.gensalt() 
    hash = by.hashpw(bytes, salt) 
    
    return hash
    
    
def decode_hash_function(password,hash):
    userBytes = password.encode('utf-8') 
    
    return by.checkpw(userBytes, hash) 
    
def generate_random_code():
    return "{:06d}".format(random.randint(0, 999999))