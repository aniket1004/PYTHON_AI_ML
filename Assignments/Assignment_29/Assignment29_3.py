# Copy file contents into a New file (Command Line Input)
import os
import sys

class FileOperation:

    def __init__(self):
        self.FileName = ""

    def SetFileName(self, FileName):
        self.FileName = FileName

    def IsFileExists(self):
        if os.path.exists(self.FileName):
            return True
        return False
    
    def CopyFileIntoNewFile(self, Size = None, NewFile = "Demo.txt"):
        content = None
        message = None
        fobj = None
        try:
            if self.IsFileExists():
                AbsPath = None
                if not(os.path.isabs(self.FileName)):
                    AbsPath = os.path.abspath(self.FileName)
                else:
                    AbsPath = self.FileName
                
                fobj = open(AbsPath, "r")
                if Size is None:
                    content = fobj.read()
                else :
                    content = fobj.read(Size)
                
                fobj.close()

                fobj = open(NewFile, "w")
                fobj.write(content)
                message = f"Contents successfully copied from file {self.FileName} to {NewFile}"
            else:
                message = "There is no such file."
        except Exception as eobj:
            message = eobj
        finally:
            if fobj is not None and not(fobj.closed):
                fobj.close()
        
        return message

def main():
    """
    Write a program which accepts an existing file name through command line arguments, 
    creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt
    """
    if len(sys.argv) != 2 :
        print("Invalid command line arguments")
        print("Please pass file name as command line")
    else:
        fobj = FileOperation()

        fobj.SetFileName(sys.argv[1])
        
        message = fobj.CopyFileIntoNewFile()
        print(message)
    
if __name__ == "__main__":
    main()