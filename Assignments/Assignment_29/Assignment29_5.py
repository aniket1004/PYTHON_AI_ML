import os
import sys


def CountStringFrequency(FileName, String):
    fobj = None
    Count = 0

    if os.path.exists(FileName):
        Fname = FileName
        if not(os.path.isabs(FileName)):
            Fname = os.path.abspath(FileName)
        fobj = open(Fname, "r")
        
        for line in fobj:
            #print(line.count(String))
            words = line.split(" ")
            for word in words:
                if word.replace("\n", "") == String:
                    Count += 1
        
        return "success", Count
    else:
        return f"There is no such file {FileName}", None

def main():
    """
    Write a program which accepts a file name and one string from the user and returns the frequency
    of that string in the file
    """
    if len(sys.argv) != 3 :
        print("Invalid command line arguments")
        print("Please pass file name and string as command line arguments")
    else:
        Message, Count = CountStringFrequency(sys.argv[1], sys.argv[2])
        if Count is not None:
            substr = "time" if Count < 2 else "times"
            print(f"{Count} {substr} \"{sys.argv[2]}\" appears in file {sys.argv[1]}")
        else:
            print(Message)
    
if __name__ == "__main__":
    main()