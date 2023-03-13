import os
from cryptography.fernet import Fernet


def file_encryption(file_path, encryption_key):
    """
    A function that encrypts the given file.
    """
    f = Fernet(encryption_key)

    with open(file_path, 'rb') as file:
        data = file.read()

    encrypted_data = f.encrypt(data)

    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def generateKey():
    encryption_key = Fernet.generate_key()
    with open("key.txt", "wb") as k:
        k.write(encryption_key)
        k.close()
    return encryption_key
    
