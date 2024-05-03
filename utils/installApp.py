import os
from colorama import Fore, Style

from utils.clearWindow import resetWindow
from utils.filesInfo import FileInfo
from utils.validationInput import InputValidation

def installAppToDevice(error: str):
    resetWindow()

    print("========================== " + Fore.YELLOW + '\033[1m' + "Install" + Style.RESET_ALL + " ==========================")
    print("")
    print("Install App")
    print("")
    print(Fore.RED + '\033[1m' + "Note:"+ Style.RESET_ALL + " make sure that USB Debugging on the device is on.")

    if error != "":
        print("")
        print(error)

    print("Select app to install: ")
    print("")

    builds = FileInfo("./output/signed", ".apks")
    appResults = builds.ListFiles()

    appSelection = input("Select app: ")

    wrongValidation = InputValidation(str(appSelection))

    isValidated = wrongValidation.IsNumberOnly()

    if (isValidated == False):
        installAppToDevice(Fore.RED + "Only number allowed.\n" + Style.RESET_ALL)
    
    correctAppSelection = int(appSelection) - 1

    appLocation = ""

    if (appResults[correctAppSelection]):
        appFile = dict(appResults[correctAppSelection])

        appLocation = str(appFile["fileLocation"])

    print("")
    command = "java -jar ./lib/bundletool.jar install-apks --apks=" + appLocation

    installApp = os.system(command)

    from app import Welcome

    if (installApp < 1):
        print("")
        print(Fore.GREEN + '\033[1m' + "App installed successful, check device." + Style.RESET_ALL)
        print("")
        input("Press Enter/Return to continue...")
        Welcome("")

    else:
        print("")
        print(Fore.RED + '\033[1m' + "Error: App installed unsuccessful" + Style.RESET_ALL)
        print("")
        sel = input("Press r to retry or Enter/Return to quit: ")

        if (sel == "r"):
            installAppToDevice("")
        
        else:
            Welcome("")