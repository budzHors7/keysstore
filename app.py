import os
from sys import exit
from colorama import Fore, Style

from utils.clearWindow import resetWindow
from utils.createNewKeyStore import newKeyStore
from utils.signApp import signYourApp
from utils.installApp import installAppToDevice
from utils.checkRequirements import checkPackages
from utils.validationInput import InputValidation

def Welcome(error: str):
    resetWindow()

    print(Fore.GREEN + '\033[1m' + "KeysStore v1.1.0")
    print(Fore.GREEN + '\033[1m' + "\nOpen Source Tool for creating Android KeyStore, Sign your \nApp with your keystore & Install your Android Build without \nusing Android Studio.")
    print(Style.RESET_ALL)

    print("Created by " + '\033[1m' + Fore.BLUE + "budzHors7 (https://github.com/budzHors7)" + Style.RESET_ALL)

    print("\nSelect option(s) below to continue")

    if error != "":
        print("")
        print(Fore.RED + error)

    print(Style.RESET_ALL)
    print("============================ " + Fore.YELLOW + '\033[1m' + "Options" + Style.RESET_ALL + " ============================")
    print("")
    print("1: Create new keystore \t\t\t 2: Sign your app")
    print("-----------------------------------------------------------------")
    print("3: Install signed app \t\t\t 4: Check requirements")
    print("-----------------------------------------------------------------")
    print("5: Quit App")
    print("")
    print("=================================================================")
    print("")

    selection = str(input("Select Menu : "))

    wrongValidation = InputValidation(selection)

    isValidated = wrongValidation.IsNumberOnly()

    if (isValidated == False):
        Welcome(Fore.RED + "Wrong Selection, only 1-5 available as options." + Style.RESET_ALL)

    selection = int(selection)

    if selection == 1:
        newKeyStore("")

    elif selection == 2:
        signYourApp("")

    elif selection == 3:
        installAppToDevice("")

    elif selection == 4:
        checkPackages()

    elif selection == 5:
        os.system('cls')
        exit()
    
    else:
        Welcome("Wrong Selection, only 1-5 available as options.")

Welcome("")