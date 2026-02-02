
def main():
    try:
        open("Demo.txt")
        print("File gets successfully opened")

    except FileNotFoundError as fobj:
        print("Unable to open file as there is no such file.")
        
    finally:
        print("End of application")

if __name__ == "__main__":
    main()