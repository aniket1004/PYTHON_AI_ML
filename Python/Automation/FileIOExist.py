import os

def main():
    FileName = input("Enter the name of the file : ")
    
    Ret = os.path.exists(FileName)
    if Ret:
        fobj = open(FileName, "r")
        print("File gets successfully opened")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()