import bcrypt as by
import random

#auxuliar functions

#codificar a hash
def encode_hash_function(password):
    
    bytes = password.encode('utf-8') 
    salt = by.gensalt() 
    hash = by.hashpw(bytes, salt) 
    
    return hash
#chekear si el hash corresponde a la constraseña indicada True/false
def decode_hash_function(password,hash):
    userBytes = password.encode('utf-8') 
    
    return by.checkpw(userBytes, hash) 
#geneerar codigo de 6 digitos para venta   
def generate_random_code():
    return "{:06d}".format(random.randint(0, 999999))