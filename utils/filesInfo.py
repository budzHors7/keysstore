from os import listdir, path
from colorama import Fore, Style

class FileInfo():

    def __init__(self, fileDir: str, fileType: str) -> None:
        self.fileDir = fileDir
        self.fileType = fileType

    def ListFiles(self):
        fileNo = 0

        fileObject = {
            "id": "",
            "fileName": "",
            "fileLocation": ""
        }

        filesResult = [fileObject]
        filesResult.clear()

        for file in listdir(self.fileDir):
            if file.endswith(self.fileType):
                fileNo = fileNo + 1
                print(path.join(str(fileNo) + ": " + Fore.GREEN + '\033[1m' + file + Style.RESET_ALL))
                print("")

                fileObject = {
                    "id": str(fileNo),
                    "fileName": str(file),
                    "fileLocation": str(path.join(self.fileDir, file))
                }

                filesResult.append(fileObject)

        return filesResult
