# Open the file and display the entire contents on the console.
# Display the contents
import os

def ReadFile(FileName):
    fobj = None
    content = None
    message = None
    try:
        if os.path.exists(FileName):
            AbsPath = None
            if not(os.path.isabs(FileName)):
                AbsPath = os.path.abspath(FileName)
            else:
                AbsPath = FileName
            
            fobj = open(AbsPath, "r")
            content = fobj.read()
            message = f"Contents of given file {FileName} is : "

        else:
            message = "There is no such file."
    except Exception as eobj:
        message = eobj
    finally:
        if fobj is not None:
            fobj.close()
    return (message, content)

def main():
    """
    Write a program which accepts a file name from the user, opens that file, 
    and displays the entire contents on the console.
    """
    FileName = input("Enter the file name : ")
    Message, Content = ReadFile(FileName)
    print(Message)
    if Content is not None:
        print(Content)

if __name__ == "__main__":
    main()
