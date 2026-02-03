import os

def DisplayFile(FileName):
    if os.path.exists(FileName):
        Fname = FileName
        if not(os.path.isabs(FileName)):
            Fname = os.path.abspath(FileName)
        fobj = None
        try:
            fobj = open(Fname, "r")
            line = fobj.readline()
            while len(line) > 0:
                print(line, end="")
                line = fobj.readline()

        except Exception as eobj:
            print(eobj)
        finally:
            if fobj is not None and not(fobj.closed):
                fobj.close()
    else:
        print("There is no such a file")

def main():
    """
    Write a program which accepts a file name from the user 
    and displays the contents of the file line by line on the screen
    """
    FileName = input("Enter the file name : ")
    DisplayFile(FileName)
    
if __name__ == "__main__":
    main()