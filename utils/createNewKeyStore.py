import os
from os import path, makedirs
from colorama import Fore, Style

from utils.clearWindow import resetWindow

def newKeyStore():
    resetWindow()

    print("========================== " + Fore.YELLOW + '\033[1m' + "Options" + Style.RESET_ALL + " ==========================")
    print("")
    print("Creating a new KeyStore (*.keystore)")
    print("")
    keyName = str(input("Enter name for your key: "))

    print("")
    alias = str(input("Enter Alias for the key: "))

    print("")
    validity = str(input("Enter number of days for key: "))

    location = "./output/keys/"

    print("Creating a New Keystore for Android Build...")
    print("")

    if not path.exists("./output/keys/"):
        makedirs("./output/keys/")

    command = "keytool -genkey -v -keystore " + location + keyName + ".keystore -alias " + alias + " -keyalg RSA -keysize 2048 -validity " + validity

    rValue = os.system(command)
    
    if rValue == 0:
        print("")
        print(Fore.GREEN + '\033[1m' + "Keystore created successful" + Style.RESET_ALL)
        print("")

        input("Press Enter/Return to continue...")

        from app import Welcome
        Welcome("")

    else:
        print("")
        print(Fore.RED + '\033[1m' + "Error: Keystore created unsuccessful" + Style.RESET_ALL)
        print("")
        input("Press Enter/Return to retry...")
        newKeyStore()