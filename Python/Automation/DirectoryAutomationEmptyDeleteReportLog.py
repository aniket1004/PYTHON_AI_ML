import sys
import os
           
def DirectoryScanner(DirName = "Marvellous"):

    Border = "-" * 50
    fobj = open("Marvellous.log", "w")
    
    fobj.write(Border + "\n")
    fobj.write("This is log file created by marvellous automation." + "\n")
    fobj.write("This is directory cleaner script." + "\n")
    fobj.write(Border + "\n")
    Ret = False

    Ret = os.path.exists(DirName)
    if not(Ret):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if not(Ret):
        print("It is not a directory")
        return
    
    FileCount = 0
    EmptyFileCount = 0
    for FolderNames, SubFolderNames, FileNames in os.walk(DirName):
        FileCount += len(FileNames)
        for Fname in FileNames:
            Fname = os.path.join(FolderNames, Fname)
            # print("File name : ", Fname)
            # print("File size : ", os.path.getsize(Fname), "bytes")
            if os.path.getsize(Fname) == 0: # Empty File
                EmptyFileCount += 1
                os.remove(Fname)
    
    fobj.write("Total files scanned :" + str(FileCount) + "\n")
    fobj.write("Total empty files found :" + str(EmptyFileCount) + "\n")
    fobj.write(Border + "\n")

    fobj.close()

def main():
    Border = "-" * 50

    print(Border)
    print("-------- Marvellous Directory Automation ---------")
    print(Border)
    
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        return

    DirName = sys.argv[1]
    DirectoryScanner(DirName)

    print(Border)
    print("-------- Marvellous Directory Automation ---------")
    print(Border)

if __name__ == "__main__":
    main()