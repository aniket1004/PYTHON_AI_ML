import os
import sys

def SearchWordInFile(FileName, SearchWord):
    isFound = False

    if os.path.exists(FileName):
        Fname = FileName
        if not(os.path.isabs(FileName)):
            Fname = os.path.abspath(FileName)
        fobj = None
        try:
            fobj = open(Fname, "r")
            line = fobj.readline()
            while len(line) > 0:
                words = line.split(" ")
                for word in words:
                    if SearchWord == word.replace("\n", ""):
                        isFound = True
                        break

                if isFound:
                    break

                line = fobj.readline()
            
            if isFound:
                print(f"Word {SearchWord} found in {os.path.basename(Fname)}")
            else:
                print(f"Word {SearchWord} not found in {os.path.basename(Fname)}")

        except Exception as eobj:
            print(eobj)
        finally:
            if fobj is not None and not(fobj.closed):
                fobj.close()
    else:
        print("There is no such a file")

def main():
    """
    Write a program which accepts a file name and a word from the user and 
    checks whether that word is present in the file or not.
    """
    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        print("Please enter File name and word that you want search")
        return
    
    FileName = sys.argv[1]
    Word = sys.argv[2]
    SearchWordInFile(FileName=FileName, SearchWord=Word)

if __name__ == "__main__":
    main()