import hashlib
import os

def CalculateChecksum(FileName):
    fobj = open(FileName, "rb")
    
    hobj = hashlib.md5()
    
    Buffer = fobj.read(1024)

    while len(Buffer) > 0:
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    
    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(DirName = "Marvellous"):
    Ret = os.path.exists(DirName)
    if not(Ret):
        print("There is no such directory")
        return
    Ret = os.path.isdir(DirName)
    if not(Ret):
        print("It is not a directory")
        return
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):

        for Fname in FileName:
            Fname = os.path.join(FolderName, Fname)
            Checksum = CalculateChecksum(Fname)
            print(f"File name : {Fname} and Checksum : {Checksum}")

def main():
    DirectoryWatcher()

if __name__ == "__main__":
    main()