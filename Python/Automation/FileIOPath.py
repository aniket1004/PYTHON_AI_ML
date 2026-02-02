import os

def main():
    FileName = input("Enter the name of the file : ")
    
    Ret = os.path.isabs(FileName)

    if Ret:
        print("It is absolute path")
    else:
        print("It is relative path")

if __name__ == "__main__":
    main()