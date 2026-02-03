import os

def CountWords(FileName):
    Message = None
    Count = 0
    if os.path.exists(FileName):
        Fname = FileName
        if not(os.path.isabs(FileName)):
            Fname = os.path.abspath(FileName)
        fobj = None
        try:
            fobj = open(Fname, "r")
            for line in fobj:
                words = line.split(" ")
                Count += len(words)

        except Exception as eobj:
            Message = eobj
        finally:
            if fobj is not None and not(fobj.closed):
                fobj.close()
    else:
        Message = "There is no such a file"

    return Message, Count

def main():
    """
    Write a program which accepts a file name from the user and counts the total number of words in that file.
    """
    FileName = input("Enter the file name : ")
    Message, Count = CountWords(FileName)
    if Message is not None:
        print(Message)
    else:
        print(f"Total number of words in file {FileName} : ", Count)

if __name__ == "__main__":
    main()