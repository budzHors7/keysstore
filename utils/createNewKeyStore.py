from os import path, makedirs
from colorama import Fore, Style
from subprocess import call

from utils.clearWindow import resetWindow
from utils.validationInput import InputValidation

def newKeyStore(error: str):
    resetWindow()

    print("========================== " + Fore.YELLOW + '\033[1m' + "Options" + Style.RESET_ALL + " ==========================")
    print("")
    print("Creating a new KeyStore (*.keystore)")
    print("")

    if error != "":
        print("")
        print(error)

    print("")
    keyName = str(input("Enter name for your key: "))

    wrongValidation = InputValidation(keyName)

    isValidated = wrongValidation.IsTextOnly()

    if (isValidated == False):
        newKeyStore(Fore.RED + "Only alphabet characters are allowed plus an underscore (_)" + Style.RESET_ALL + "\n\nAllowed:" + Fore.GREEN +" app_name or AppName" + Style.RESET_ALL + "\nNot Allowed:" + Fore.RED + " app_name1 or AppName1" + Style.RESET_ALL)

    print("")
    alias = str(input("Enter Alias for the key: "))

    wrongValidation = InputValidation(alias)

    isValidated = wrongValidation.IsTextOnly()

    if (isValidated == False):
        newKeyStore(Fore.RED + "Only alphabet characters are allowed" + Style.RESET_ALL + "\n\nAllowed:" + Fore.GREEN +" AliasName" + Style.RESET_ALL + "\nNot Allowed:" + Fore.RED + " alias_name" + Style.RESET_ALL)

    print("")
    validity = str(input("Enter number of days for key: "))

    wrongValidation = InputValidation(validity)

    isValidated = wrongValidation.IsNumberOnly()

    if (isValidated == False):
        newKeyStore(Fore.RED + "Only number (0-9) in days are allowed" + Style.RESET_ALL)

    print("")
    print("Creating a New Keystore for Android Build...")
    print("")

    if not path.exists("./output/keys/"):
        makedirs("./output/keys/")

    print("")
    command = [
        "keytool",
        "-genkey",
        "-v",
        "-keystore",
        f"./output/keys/{keyName}.keystore",
        "-alias",
        alias,
        "-keyalg",
        "RSA",
        "-keysize",
        "2048",
        "-validity",
        validity
    ]

    rValue = call(command)

    from app import Welcome
    
    if rValue == 0:
        print("")
        print(Fore.GREEN + '\033[1m' + "Keystore created successful" + Style.RESET_ALL)
        print("")

        input("Press Enter/Return to continue...")

        Welcome("")

    else:
        print("")
        print(Fore.RED + '\033[1m' + "Error: Keystore created unsuccessful" + Style.RESET_ALL)
        print("")
        sel = input("Press r to retry or Enter/Return to quit: ")

        if (sel == "r"):
            newKeyStore("")
        
        else:
            Welcome("")