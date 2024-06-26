import os
from os import system
from platform import system

def resetWindow():
    if system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')