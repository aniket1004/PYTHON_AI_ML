import FileModule
from FileLogger import FileLogger
import time
import sys
import os

loggerObj = FileLogger("Assignment32_2.log")

def DirectoryFileDuplicateSearch(DirectoryName):
    if DirectoryName  is None or DirectoryName == "":
        print("Invalid directory name provided")
        return
    
    if not(os.path.isdir(DirectoryName)):
        print("There is no such directory")
        return
    try:
        loggerObj.WriteLine(f"Duplicate files under directory {DirectoryName} are : ")
        DuplicateFiles = {}

        for Folders, SubFolders, Files in os.walk(DirectoryName):

            for FileName in Files:
                Fname = os.path.join(Folders, FileName)
                CheckSum = FileModule.GetCheckSum(Fname)
                if CheckSum in DuplicateFiles.keys():
                    DuplicateFiles[CheckSum].append(Fname)
                else:
                    DuplicateFiles[CheckSum] = [Fname]

        Duplicates = list(filter(lambda F : len(F) > 1, DuplicateFiles.values()))
        Counter = 0
        for FileNames in Duplicates:
            Counter += 1
            loggerObj.WriteLine(f"{Counter})")
            for DupFileName in FileNames:
                loggerObj.WriteLine(f"{DupFileName}")

    except Exception as eobj:
        loggerObj.WriteLine(str(eobj))


def main():
    global loggerObj
    #border = "-" * 50
    loggerObj.WriteBorder()
    loggerObj.WriteLine("------------- Marvellous  Automation -------------")
    loggerObj.WriteBorder()

    Start = time.time()
    loggerObj.WriteLine(f"Execution of script started on : {time.ctime()}", End="\n\n")

    if len(sys.argv) == 2:
        
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This automation script accept directory name and write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory.")

        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("ScriptName.py Argument1")
            print("Argument1 : Directory Name")
        
        else:
            DirectoryName = sys.argv[1]

            DirectoryFileDuplicateSearch(DirectoryName=DirectoryName)
    else:
        print("Invalid number of command line arguments")   
        print("Use the given flag as:")
        print("--U : Use to display the usage")
        print("--H : Use to display the help")

    End = time.time()
    RequiredTime = End-Start
    loggerObj.WriteLine(f"\nExecution of script ended on : {time.ctime()}")
    loggerObj.WriteLine(f"\nTotal time required (in seconds) : {RequiredTime}")

    loggerObj.WriteNextLine()
    loggerObj.WriteBorder()
    loggerObj.WriteLine("----------- Thank you for using our script--------")
    loggerObj.WriteLine("------------- Marvellous Infosystems -------------")
    loggerObj.WriteNextLine()

if __name__ == "__main__":
    main()