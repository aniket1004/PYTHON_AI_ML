

def main():
    """
    Docstring for main
    Accept one number and display below pattern.
    input : 5
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    """
    try :
        print("Enter the number:", end=" ")
        num = int(input())

        for _ in range(num):
            for _ in range(num):
                print("*", end=" ")
            print("")

    except ValueError as vobj:
        print("Please enter numeric value")
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()