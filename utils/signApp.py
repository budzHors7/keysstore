import os
from os import path, makedirs, listdir
from colorama import Fore, Style

from utils.clearWindow import resetWindow

def signYourApp():
    resetWindow()

    print("========================== " + Fore.YELLOW + '\033[1m' + "Sign App Build" + Style.RESET_ALL + " ==========================")
    print("")
    print(Fore.RED + '\033[1m' + "Note:" + Style.RESET_ALL + " to sign your build, make sure you place the file (*.abb) \n      inside the folder builds.")
    print("")

    if not path.exists("./builds"):
        makedirs("./builds")

    if not path.exists("./output/keys"):
        makedirs("./output/keys")

    print("List of build: ")
    print("")

    buildNo = 0

    buildObject = {
        "id": "",
        "fileName": "",
        "fileLocation": ""
    }

    buildsResults = [buildObject]
    buildsResults.clear()

    for buildsFile in listdir("./builds"):
        if buildsFile.endswith(".aab"):
            buildNo = buildNo + 1
            print(path.join(str(buildNo) + ": " + Fore.GREEN + '\033[1m' + buildsFile + Style.RESET_ALL))
            print("")

            buildObject = {
                "id": str(buildNo),
                "fileName": str(path.join(buildsFile)),
                "fileLocation": str(path.join("./builds", buildsFile))
            }

            buildsResults.append(buildObject)

    buildSelection = int(input("Select Build: "))
    print("")

    keysNo = 0

    keysObject = {
        "id": "",
        "fileName": "",
        "fileLocation": ""
    }

    keysResults = [keysObject]
    keysResults.clear()

    for keysFile in listdir("./output/keys"):
        if keysFile.endswith(".keystore"):
            keysNo = keysNo + 1
            print(path.join(str(keysNo) + ": " + Fore.GREEN + '\033[1m' + keysFile + Style.RESET_ALL))
            print("")

            keysObject = {
                "id": str(keysNo),
                "fileName": str(path.join(keysFile)),
                "fileLocation": str(path.join("./output/keys", keysFile))
            }

            keysResults.append(keysObject)

    keySelection = int(input("Select your key: "))
    print("")

    correctBuildSelection = buildSelection - 1
    correctKeySelection = keySelection - 1

    buildLocation = ""
    keyLocation = ""
    keyName = ""

    if (buildsResults[correctBuildSelection]):
        buildFile = dict(buildsResults[correctBuildSelection])
        
        buildLocation = str(buildFile["fileLocation"])

    if (keysResults[correctKeySelection]):
        keyFile = dict(keysResults[correctKeySelection])
        
        keyName = str(keyFile["fileName"])
        keyLocation = str(keyFile["fileLocation"])
    
    buildName = input("Enter name for signed new build (*.apks): ")
    print("")

    keyAliasName = input("Enter alias name for your key -> (" + keyName + "): ")
    print("")

    keyAliasPass = input("Enter password for alias key -> (" + keyName + "): ")
    print("")

    command = "java -jar ./lib/bundletool.jar build-apks --bundle=" + buildLocation + " --output=./output/signed/" + buildName + ".apks --ks=" + keyLocation + " --ks-pass=pass:" + keyAliasPass + " --ks-key-alias=" + keyAliasName

    generateNewSignedCommand = os.system(command)

    from app import Welcome

    if (generateNewSignedCommand < 1):
        print("")
        print(Fore.GREEN + '\033[1m' + "Signed build created successful" + Style.RESET_ALL)
        print("")
        input("Press Enter/Return to continue...")
        Welcome("")

    else:
        print("")
        print(Fore.RED + '\033[1m' + "Error: Signed build created unsuccessful" + Style.RESET_ALL)
        print("")
        sel = input("Press r to retry or Enter/Return to quit")

        if (sel == "r"):
            signYourApp()
        
        else:
            Welcome("")