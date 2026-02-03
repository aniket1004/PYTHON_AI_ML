# Check File Exists in Current Directory
import os

class FileOperation:

    def __init__(self):
        self.FileName = ""

    def AcceptFileName(self):
        self.FileName = input("Enter the file name : ")

    def GetFileName(self):
        return self.FileName
        
    def IsFileExists(self, DirectoryName = ""):
        Path = self.FileName
        if DirectoryName != "":
            Path = os.path.join(DirectoryName, self.FileName)
        
        if os.path.exists(Path):
            return True
        
        return False
    
def main():
    """
    Write a program which accepts a file name from the user and 
    checks whether that file exists in the current directory or not.    
    """
    print(main.__doc__)
    fobj = FileOperation()
    fobj.AcceptFileName()

    DisplayFileName = os.path.basename(fobj.GetFileName())
    if fobj.IsFileExists():
        print(f"{DisplayFileName} is exist in current directory")
    else:
        print(f"{DisplayFileName} is not exist in current directory")

if __name__ == "__main__":
    main()
        