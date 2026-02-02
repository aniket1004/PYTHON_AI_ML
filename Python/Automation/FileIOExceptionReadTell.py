
def main():
    try:
        fobj = open("Hello.txt", "r")
        print("File gets successfully opened")

        print("Current offset is:", fobj.tell())

        Data = fobj.read(6)
        
        print("Current offset is:", fobj.tell())
        
        print("Data from file is:", Data)

        fobj.close()
    except FileNotFoundError as fobj:
        print("Unable to open file as there is no such file.")
        
    finally:
        print("End of application")
        
if __name__ == "__main__":
    main()