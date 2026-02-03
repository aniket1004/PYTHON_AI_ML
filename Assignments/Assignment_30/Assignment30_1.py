import os
class FileOperation:

    def __init__(self, FileName):
        self.FileName = FileName

    def IsFileExist(self):
        Ret = False

        if self.FileName == "":
            return Ret 
        else:
            if os.path.exists(self.FileName):
                Ret = True

        return Ret
    
    def CountLinesFromFile(self):
        Count = 0
        fobj = None
        if not(self.IsFileExist()):
            return "There is no such a file", None
        try:
            fobj = open(self.FileName, "r")
            lines = fobj.readlines()
            return "Success", len(lines)
        except Exception as eobj:
            return eobj, None
        finally:
            if fobj is not None and not(fobj.closed):
                fobj.close()
    
def main():
    """
    Write a program which accepts a file name from the user and counts how many lines are present in
    the file.
    """
    FileName = input("Enter the file name: ")
    fobj = FileOperation(FileName)
    Message, Count = fobj.CountLinesFromFile()
    if Count is None:
        print(Message)
    else:
        print(f"Total number of lines in {FileName} : ", Count)

if __name__ == "__main__":
    main()
            