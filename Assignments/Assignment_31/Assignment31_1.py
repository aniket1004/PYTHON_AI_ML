
import sys
import os
import time
import FileOperation
from FileLogger import FileLogger

loggerObj = FileLogger("Assignment31_1.log")

def DirectoryFileSearchByExtension(DirectoryName, FileExtension):
    global loggerObj
    if not(FileOperation.IsDirectoryExist(DirectoryName=DirectoryName)):
        loggerObj.WriteLine(f"There is no such directory name {DirectoryName}")
        return
    
    if FileExtension is None or FileExtension == "":
        loggerObj.WriteLine(f"Please enter valid file extension")
        return
    
    F_Extension = FileExtension.replace(".", "")
    try:
        FilesList = list()
        for Folders, SubFolders, FileNames in os.walk(DirectoryName):
    
            for Filename in FileNames:
                Fname = os.path.join(Folders, Filename)
                if os.path.isfile(Fname):
                    Extension = FileOperation.GetFileExtension(FileName=Fname)
                    if Extension == F_Extension:
                        FilesList.append(Filename)
        
        if len(FilesList) > 0:
            loggerObj.WriteLine(f"Files with extension {FileExtension} in given directory {DirectoryName} : ")
            for File in FilesList:
                loggerObj.WriteLine(File)

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
            print("This automation script accept directory name and file extension from user. Display all files with that extension.")

        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1 : Directory Name")
            print("Argument2 : File Extension")
        
        else:
            print("Use the given flag as:")
            print("--U : Use to display the usage")
            print("--H : Use to display the help")           
    elif len(sys.argv) == 3:

        DirectoryName = sys.argv[1]
        FileExtension = sys.argv[2]

        DirectoryFileSearchByExtension(DirectoryName=DirectoryName, FileExtension=FileExtension)
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