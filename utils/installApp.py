import os
from os import path, listdir
from colorama import Fore, Style

from utils.clearWindow import resetWindow

def installAppToDevice():
    resetWindow()

    print("========================== " + Fore.YELLOW + '\033[1m' + "Install" + Style.RESET_ALL + " ==========================")
    print("")
    print("Install App")
    print("")
    print("Select app to install: ")
    print("")

    appNo = 0

    appObject = {
        "id": "",
        "fileName": "",
        "fileLocation": ""
    }

    appResults = [appObject]
    appResults.clear()

    for appsFile in listdir("./output/signed"):
        if appsFile.endswith(".apks"):
            appNo = appNo + 1
            print(path.join(str(appNo) + ": " + Fore.GREEN + '\033[1m' + appsFile + Style.RESET_ALL))
            print("")

            appObject = {
                "id": str(appNo),
                "fileName": str(path.join(appsFile)),
                "fileLocation": str(path.join("./output/signed", appsFile))
            }

            appResults.append(appObject)

    appSelection = int(input("Select your key: "))
    
    correctAppSelection = appSelection - 1

    appLocation = ""

    if (appResults[correctAppSelection]):
        appFile = dict(appResults[correctAppSelection])

        appLocation = str(appFile["fileLocation"])

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
            installAppToDevice()
        
        else:
            Welcome("")