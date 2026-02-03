import os
import sys
import hashlib

def CheckSum(FileName):
    fobj = None
    hobj = hashlib.md5()

    if os.path.exists(FileName):
        Fname = FileName
        if not(os.path.isabs(FileName)):
            Fname = os.path.abspath(FileName)
        fobj = open(Fname, "rb")
        Buffer = fobj.read(1024)

        while len(Buffer) > 0:
            hobj.update(Buffer)
            Buffer = fobj.read(1024)
        
        return "success", hobj.hexdigest()
    else:
        return f"There is no such file {FileName}", None
    
def CompareTwoFiles(Filename1, Filename2):
    Message1, CheckSum1 = CheckSum(Filename1)
    Message2, CheckSum2 = CheckSum(Filename2)

    if Message1 == "success" and Message2 == "success":
        if CheckSum1 == CheckSum2:
            return True
    
    return False

def main():
    """
    Write a program which accepts an existing file name through command line arguments, 
    creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt
    """
    if len(sys.argv) != 3 :
        print("Invalid command line arguments")
        print("Please pass two file names as command line arguments")
    else:
        Ret = CompareTwoFiles(sys.argv[1], sys.argv[2])
        if Ret:
            print("Success")
        else:
            print("Failure")
    
if __name__ == "__main__":
    main()