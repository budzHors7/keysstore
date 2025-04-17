from os import path, makedirs, system
from colorama import Fore, Style

from utils.clearWindow import resetWindow
from utils.filesInfo import FileInfo
from utils.validationInput import InputValidation

def signYourApp(error: str):
    resetWindow()

    print("========================== " + Fore.YELLOW + '\033[1m' + "Sign App Build" + Style.RESET_ALL + " ==========================")
    print("")
    print(Fore.RED + '\033[1m' + "Note:" + Style.RESET_ALL + " to sign your build, make sure you place the file (*.abb) \n      inside the folder builds.")
    print("")

    if not path.exists("./builds"):
        makedirs("./builds")

    if not path.exists("./output/keys"):
        makedirs("./output/keys")

    if error != "":
        print("")
        print(error)

    print("List of build: ")
    print("")

    builds = FileInfo("./builds", ".aab")
    buildsResults = builds.ListFiles()

    buildSelection = input("Select Build: ")
    print("")

    wrongValidation = InputValidation(str(buildSelection))

    isValidated = wrongValidation.IsNumberOnly()

    if (isValidated == False):
        signYourApp(Fore.RED + "Only number allowed.\n" + Style.RESET_ALL)

    keys = FileInfo("./output/keys", ".keystore")
    keysResults = keys.ListFiles()

    keySelection = input("Select your key: ")
    print("")

    wrongValidation = InputValidation(str(keySelection))

    isValidated = wrongValidation.IsNumberOnly()

    if (isValidated == False):
        signYourApp(Fore.RED + "Only number allowed.\n" + Style.RESET_ALL)

    correctBuildSelection = int(buildSelection) - 1
    correctKeySelection = int(keySelection) - 1

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

    wrongValidation = InputValidation(buildName)

    isValidated = wrongValidation.IsTextWithNumbers()

    if (isValidated == False):
        signYourApp(Fore.RED + "Only number (0-9) & Alphabet characters (a-z/A-Z) allowed.\n" + Style.RESET_ALL)

    keyAliasName = input("Enter alias name for your key -> (" + keyName + "): ")
    print("")

    wrongValidation = InputValidation(keyAliasName)

    isValidated = wrongValidation.IsTextOnly()

    if (isValidated == False):
        signYourApp(Fore.RED + "Alphabet characters (a-z/A-Z) allowed.\n" + Style.RESET_ALL)

    keyAliasPass = input("Enter password for alias key -> (" + keyName + "): ")
    print("")

    wrongValidation = InputValidation(keyAliasPass)

    isValidated = wrongValidation.IsPassword()

    if (isValidated == False):
        signYourApp(Fore.RED + "Only number (0-9) & Alphabet characters (a-z/A-Z) allowed.\n" + Style.RESET_ALL)

    command = "java -jar ./lib/bundletool.jar build-apks --bundle=" + buildLocation + " --output=./output/signed/" + buildName + ".apks --ks=" + keyLocation + " --ks-pass=pass:" + keyAliasPass + " --ks-key-alias=" + keyAliasName

    generateNewSignedCommand = system(command)

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
            signYourApp("")
        
        else:
            Welcome("")