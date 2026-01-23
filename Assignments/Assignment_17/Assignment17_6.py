
def DisplayPattern(No):
    """
    Docstring for DisplayPattern
    Accept one number and display below pattern.
    No : 5
    * * * * *
    * * * *
    * * *
    * *
    *
    
    :param No: Numeric Value

    """
    for i in range(No, 0, -1):
        
        for j in range(i):
            print("*", end="  ")
        
        print("")

def main():
   
    try :
        print("Enter the number:", end=" ")
        num = int(input())

        DisplayPattern(num)
       
    except ValueError as vobj:
        print("Please enter numeric value")
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()
