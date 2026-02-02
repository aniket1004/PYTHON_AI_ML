
def main():
    try:
        fobj = open("Hello.txt", "w")
        print("File gets successfully opened")

        fobj.write("Jay Ganesh Marvellous...")

        fobj.close()
    except FileNotFoundError as fobj:
        print("Unable to open file as there is no such file.")
        
    finally:
        print("End of application")
        
if __name__ == "__main__":
    main()