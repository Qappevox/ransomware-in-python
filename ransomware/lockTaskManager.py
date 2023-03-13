import os
import platform

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
    with open("platform.json", "r") as pl:
        j = json.load(pl)
        j = j["platform"]
        pl.close()
    if j == "Windows":
        windows()
    elif j == "Linux":
        linux()
