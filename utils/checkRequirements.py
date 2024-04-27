import os
from colorama import Fore, Style

from utils.clearWindow import resetWindow

def checkPackages():
    resetWindow()

    print("========================== " + Fore.YELLOW + '\033[1m' + "Requirements" + Style.RESET_ALL + " ==========================")
    print("")
    print("All check below must be green to indicate that all required \npackages are installed.")
    print("")
    print("-----------------------------------------------------------------")
    print('\033[1m' + "1: Java")
    print("")

    javaCommand = os.system("java --version")
    
    if (javaCommand < 1):
        print(Fore.GREEN + "\nFound" + Style.RESET_ALL)

    else:
        print(Fore.RED + "\nNot Found" + Style.RESET_ALL)

    print("-----------------------------------------------------------------")
    print('\033[1m' + "2: Adb - Android Debug Bridge")
    print("")

    adbCommand = os.system("adb --version")
    
    if (adbCommand < 1):
        print(Fore.GREEN + "\nFound" + Style.RESET_ALL)

    else:
        print(Fore.RED + "\nNot Found" + Style.RESET_ALL)

    print("-----------------------------------------------------------------")
    print('\033[1m' + "3: Bundletool")
    print("")

    adbCommand = os.system("java -jar ./lib/bundletool.jar version")
    
    if (adbCommand < 1):
        print(Fore.GREEN + "\nFound" + Style.RESET_ALL)

    else:
        print(Fore.RED + "\nNot Found" + Style.RESET_ALL)

    print("-----------------------------------------------------------------")
    input("Press Enter/Return to continue...")
    print("")
    from app import Welcome
    Welcome("")