import os

def CopyFile(SrcFileName, DestFileName):
    if os.path.exists(SrcFileName):
        Fname = SrcFileName
        if not(os.path.isabs(SrcFileName)):
            Fname = os.path.abspath(SrcFileName)
        fobj = None
        try:
            fobj = open(Fname, "r")
            wobj = open(DestFileName, "w")

            line = fobj.read(1024)
            while len(line) > 0:
                wobj.write(line)
                line = fobj.read(1024)
            print(f"Contents of {os.path.basename(SrcFileName)} copied into {os.path.basename(DestFileName)}")
        except Exception as eobj:
            print(eobj)
        finally:
            if fobj is not None and not(fobj.closed):
                fobj.close()
            if wobj is not None and not(wobj.closed):
                wobj.close()
    else:
        print("There is no such a file")

def main():
    """
    Write a program which accepts two file names from the user.
    First file is an existing file
    Second file is a new file
    Copy all contents from the first file into the second file.
    """
    SrcFileName = input("Enter the first file name (Existing File) : ")
    DestFileName = input("Enter the second file name (New file) : ")

    CopyFile(SrcFileName, DestFileName)
    
if __name__ == "__main__":
    main()