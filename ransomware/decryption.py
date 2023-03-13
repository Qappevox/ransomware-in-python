from cryptography.fernet import Fernet
def file_decryption(file_path, encryption_key):
    """
    A function that decrypts the given file.
    """
    f = Fernet(encryption_key)

    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def getKey():
    with open("key.txt", "rb") as k:
        encryption_key = k.read()
        k.close()
    print("encryption key --> {0}".format(encryption_key))
    return encryption_key
