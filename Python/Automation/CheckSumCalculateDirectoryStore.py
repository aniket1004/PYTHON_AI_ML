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

def FindDuplicate(DirName = "Marvellous"):
    Ret = os.path.exists(DirName)
    if not(Ret):
        print("There is no such directory")
        return
    Ret = os.path.isdir(DirName)
    if not(Ret):
        print("It is not a directory")
        return
    Duplicate = {}
    for FolderName, SubFolderName, FileName in os.walk(DirName):

        for Fname in FileName:
            Fname = os.path.join(FolderName, Fname)
            Checksum = CalculateChecksum(Fname)
            if Checksum in Duplicate:
                Duplicate[Checksum].append(Fname)
            else:
                Duplicate[Checksum] = [Fname]
    
    return Duplicate

def DeleteDuplicate(Path = "Marvellous"):
    MyDict = FindDuplicate(Path)
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))
    Count = 0
    Cnt = 0
    for value in Result:
        for subvalue in value:
            Count += 1
            if Count > 1 :
                os.remove(subvalue)
                print("Deleted file : ", subvalue)
                Cnt += 1
        Count = 0
    print("Total deleted files: ", Cnt)

def DisplayResult(MyDict):
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))
    Count = 0

    for value in Result:
        for subvalue in value:
            Count += 1
            print(subvalue)
        print("Value of count is : ", Count)
        Count = 0

def main():
    DeleteDuplicate()

if __name__ == "__main__":
    main()