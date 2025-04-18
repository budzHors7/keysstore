from os import path, makedirs
from subprocess import call
import requests
import time
from datetime import timedelta
from colorama import Fore, Style

from utils.clearWindow import resetWindow

def download_bundletool():
    resetWindow()
    
    print("======================= " + Fore.YELLOW + '\033[1m' + "Download Bundletool" + Style.RESET_ALL + " =======================")
    print("")
    
    # Create lib directory if it doesn't exist
    if not path.exists("./lib"):
        makedirs("./lib")
    
    # Get latest release info from GitHub API
    print("Fetching latest release information...")
    api_url = "https://api.github.com/repos/google/bundletool/releases/latest"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        release_data = response.json()
        latest_version = release_data["tag_name"]
        
        # Find the .jar asset
        jar_asset = None
        for asset in release_data["assets"]:
            if asset["name"].endswith(".jar"):
                jar_asset = asset
                break
        
        if not jar_asset:
            print(Fore.RED + "Error: Could not find bundletool.jar in the latest release." + Style.RESET_ALL)
            input("\nPress Enter/Return to continue...")
            return False
        
        download_url = jar_asset["browser_download_url"]
        file_size_bytes = jar_asset["size"]
        file_size_mb = file_size_bytes / (1024 * 1024)
        
        print(f"\nFound bundletool {latest_version}")
        print(f"File size: {file_size_mb:.2f} MB")
        
        # Confirm download
        confirmation = input("\nDownload this version? (y/n): ")
        if confirmation.lower() != 'y':
            print("\nDownload canceled.")
            input("\nPress Enter/Return to continue...")
            return False
        
        print(f"\nDownloading bundletool {latest_version}...\n")
        
        # Start download with progress tracking
        start_time = time.time()
        response = requests.get(download_url, stream=True)
        response.raise_for_status()
        
        downloaded_bytes = 0
        chunk_size = 1024 * 8  # 8KB chunks
        
        output_file_path = "./lib/bundletool.jar"
        
        with open(output_file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    file.write(chunk)
                    downloaded_bytes += len(chunk)
                    
                    # Calculate progress and ETA
                    progress = (downloaded_bytes / file_size_bytes) * 100
                    elapsed_time = time.time() - start_time
                    
                    if downloaded_bytes > 0 and elapsed_time > 0:
                        download_speed = downloaded_bytes / elapsed_time  # bytes per second
                        eta_seconds = (file_size_bytes - downloaded_bytes) / download_speed if download_speed > 0 else 0
                        eta = str(timedelta(seconds=int(eta_seconds)))
                        
                        # Create progress bar
                        bar_length = 30
                        filled_length = int(bar_length * downloaded_bytes // file_size_bytes)
                        bar = '█' * filled_length + '░' * (bar_length - filled_length)
                        
                        # Calculate download speed in MB/s
                        speed_mb = download_speed / (1024 * 1024)
                        
                        # Print progress with carriage return to update in place
                        print(f"\r[{bar}] {progress:.1f}% | {downloaded_bytes/(1024*1024):.2f}/{file_size_mb:.2f} MB | {speed_mb:.2f} MB/s | ETA: {eta}", end='')
        
        # Print newline after download completes
        print("\n")
        print(Fore.GREEN + f"Download complete! Saved to {output_file_path}" + Style.RESET_ALL)
        
        # Verify download
        if path.exists(output_file_path):
            downloaded_size = path.getsize(output_file_path)
            if downloaded_size == file_size_bytes:
                print(Fore.GREEN + "\nFile verification successful!" + Style.RESET_ALL)
                input("\nPress Enter/Return to continue...")
                return True
            else:
                print(Fore.RED + "Error: File size mismatch. Download may be incomplete." + Style.RESET_ALL)
                input("\nPress Enter/Return to continue...")
                return False
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"\nError during download: {str(e)}" + Style.RESET_ALL)
        input("\nPress Enter/Return to continue...")
        return False
    
    except Exception as e:
        print(Fore.RED + f"\nUnexpected error: {str(e)}" + Style.RESET_ALL)
        input("\nPress Enter/Return to continue...")
        return False

def checkPackages():
    resetWindow()

    print("========================== " + Fore.YELLOW + '\033[1m' + "Requirements" + Style.RESET_ALL + " ==========================")
    print("")
    print("All check below must be green to indicate that all required \npackages are installed.")
    print("")
    print("-----------------------------------------------------------------")
    print('\033[1m' + "1: Java")
    print("")

    javaCommand = call(["java", "--version"])
    
    if (javaCommand < 1):
        print(Fore.GREEN + "\nFound" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\nNot Found" + Style.RESET_ALL)
        print("\nPlease install Java Development Kit (JDK) from:")
        print(Fore.BLUE + "https://www.oracle.com/java/technologies/downloads/" + Style.RESET_ALL)

    print("-----------------------------------------------------------------")
    print('\033[1m' + "2: Adb - Android Debug Bridge")
    print("")

    adbCommand = call(["adb", "--version"])
    
    if (adbCommand < 1):
        print(Fore.GREEN + "\nFound" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\nNot Found" + Style.RESET_ALL)
        print("\nPlease install Android Debug Bridge (ADB) from:")
        print(Fore.BLUE + "https://developer.android.com/tools/releases/platform-tools" + Style.RESET_ALL)

    print("-----------------------------------------------------------------")
    print('\033[1m' + "3: Bundletool")
    print("")

    # Check if lib directory exists
    if not path.exists("./lib"):
        makedirs("./lib")

    bundletool_exists = path.exists("./lib/bundletool.jar")
    
    if bundletool_exists:
        bundletoolCommand = call(["java", "-jar", "./lib/bundletool.jar", "version"])
        
        if (bundletoolCommand < 1):
            print(Fore.GREEN + "\nFound" + Style.RESET_ALL)
        else:
            print(Fore.RED + "\nFile exists but unable to execute" + Style.RESET_ALL)
            print("\nThe bundletool.jar file might be corrupted. Consider downloading again.")
    else:
        print(Fore.RED + "\nNot Found" + Style.RESET_ALL)
        print("\nBundletool is required but not found in the lib directory.")
    
    print("-----------------------------------------------------------------")
    print("Options:")
    print("")
    print("1: Download Bundletool       2: Return to main menu")
    print("")
    
    choice = input("Select option: ")
    
    if choice == "1":
        download_bundletool()
        # Return to check requirements after download
        checkPackages()
    else:
        from app import Welcome
        Welcome("")