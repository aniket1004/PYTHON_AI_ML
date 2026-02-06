
import sys
import os
import shutil
import time
import FileOperation
from FileLogger import FileLogger

loggerObj = FileLogger("Assignment31_3.log")

def DirectoryFileCopyToAnotherDirectory(DirectoryName,  NewDirectory):
    global loggerObj
    if not(FileOperation.IsDirectoryExist(DirectoryName=DirectoryName)):
        loggerObj.WriteLine(f"There is no such directory name {DirectoryName}")
        return
    
    if NewDirectory is None or NewDirectory == "":
        loggerObj.WriteLine(f"Please enter valid new directory name")
        return
    
    if not(FileOperation.IsDirectoryExist(DirectoryName=NewDirectory)):
        os.mkdir(NewDirectory)
    
    try:
        Count = 0
        for Folders, SubFolders, FileNames in os.walk(DirectoryName):

            for FileName in FileNames:
                Fname = os.path.join(Folders, FileName)
                if os.path.isfile(Fname):
                    try:
                        NewFile = os.path.join(NewDirectory, FileName)
                        shutil.copy(Fname, NewFile)
                        loggerObj.WriteLine(f"{Fname} successfully copied into destination {NewFile}")
                        Count += 1
                    except shutil.SameFileError as sobj:
                        loggerObj.WriteLine(f"{Fname} is already exist in destination directory {NewDirectory}")
                    except PermissionError as pobj:
                        loggerObj.WriteLine(f"Access Denied")
                    except Exception as eobj:
                        loggerObj.WriteLine(f"Exception occured for file {Fname}")
                        loggerObj.WriteLine(str(eobj))
                        
            break

        loggerObj.WriteNextLine()
        loggerObj.WriteLine(f"{Count} Files successfully copied from directory {DirectoryName} to {NewDirectory} ")

    except Exception as eobj:
        loggerObj.WriteLine(str(eobj))

def main():
    global loggerObj
    #border = "-" * 50
    loggerObj.WriteBorder()
    loggerObj.WriteLine("------------- Marvellous  Automation -------------")
    loggerObj.WriteBorder()

    Start = time.time()
    loggerObj.WriteLine(f" Execution of script started on : {time.ctime()}")

    if len(sys.argv) == 2:
        
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This automation script  accept two directory names. Copy all files from first directory into second directory.")

        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1 : Source Directory Name")
            print("Argument2 : Destination Directory Name")
        
        else:
            print("Use the given flag as:")
            print("--U : Use to display the usage")
            print("--H : Use to display the help")           
    elif len(sys.argv) == 3:

        DirectoryName = sys.argv[1]
        NewDirectoryName = sys.argv[2]

        DirectoryFileCopyToAnotherDirectory(DirectoryName=DirectoryName, NewDirectory=NewDirectoryName)

    else:
        print("Invalid number of command line arguments")   
        print("Use the given flag as:")
        print("--U : Use to display the usage")
        print("--H : Use to display the help")

    End = time.time()
    RequiredTime = End-Start
    loggerObj.WriteLine(f" Execution of script ended on : {time.ctime()}")
    loggerObj.WriteLine(f"Total time required (in seconds) : {RequiredTime}")
    
    loggerObj.WriteNextLine()
    loggerObj.WriteBorder()
    loggerObj.WriteLine("----------- Thank you for using our script--------")
    loggerObj.WriteLine("------------- Marvellous Infosystems -------------")
    loggerObj.WriteNextLine()


if __name__== "__main__":
    main()