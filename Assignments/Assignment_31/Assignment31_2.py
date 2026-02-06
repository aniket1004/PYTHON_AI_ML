
import sys
import os
import time
import FileOperation
from FileLogger import FileLogger

loggerObj = FileLogger("Assignment31_2.log")

def DirectoryFileRenameByExtension(DirectoryName, OldFileExtension, NewFileExtension):
    global loggerObj
    if not(FileOperation.IsDirectoryExist(DirectoryName=DirectoryName)):
        loggerObj.WriteLine(f"There is no such directory name {DirectoryName}")
        return
    
    if OldFileExtension is None or OldFileExtension == "":
        loggerObj.WriteLine(f"Please enter valid existing file extension")
        return
    if NewFileExtension is None or NewFileExtension == "":
        loggerObj.WriteLine(f"Please enter valid new file extension")
        return
    
    try:
        Old_EXT = OldFileExtension.replace(".", "")
        New_EXT = NewFileExtension.replace(".", "")

        Count = 0
        for Folders, SubFolders, FileNames in os.walk(DirectoryName):

            for FileName in FileNames:
                Fname = os.path.join(Folders, FileName)
                if os.path.isfile(Fname):
                    Extension = FileOperation.GetFileExtension(FileName=Fname)
                    if Extension == Old_EXT:
                        Name = FileOperation.GetFileNameWithoutExtension(Fname)
                        NewName = f"{Name}.{New_EXT}"
                        os.rename(Fname, NewName)
                        loggerObj.WriteLine(f" File {Fname} is successfully renamed to {NewName}")
                        Count += 1

        loggerObj.WriteNextLine()
        if Count > 0:
            loggerObj.WriteLine(f"Successfully renamed {Count} files with old extension {OldFileExtension} to new extension {NewFileExtension} in given directory {DirectoryName} ")
        else :
            loggerObj.WriteLine(f"No files found for given extension {OldFileExtension} in given directory {DirectoryName}")
        

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
            print("This automation script accept directory name and  two file extensions from user. Rename all files with first file extension with the second file extension.")

        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("ScriptName.py Argument1 Argument2 Argument3")
            print("Argument1 : Directory Name")
            print("Argument2 : Old File Extension")
            print("Argument2 : New File Extension")
        
        else:
            print("Use the given flag as:")
            print("--U : Use to display the usage")
            print("--H : Use to display the help")           
    elif len(sys.argv) == 4:

        DirectoryName = sys.argv[1]
        OldFileExtension = sys.argv[2]
        NewFileExtension = sys.argv[3]

        DirectoryFileRenameByExtension(DirectoryName=DirectoryName, OldFileExtension=OldFileExtension, NewFileExtension=NewFileExtension)

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