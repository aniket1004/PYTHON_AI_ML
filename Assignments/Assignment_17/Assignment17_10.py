
def AdditionOfDigits(No):
    """
    Docstring for AdditionOfDigits
    Accept number from user and return addition of digits in that number.
    No : 5187934 
    Return : 37
    
    :param No: Numeric Value

    """
    Sum = 0

    while No > 0:
        Sum = Sum + (No % 10)
        No = No // 10

    return Sum


def main():
   
    try :
        print("Enter the number:", end=" ")
        num = int(input())

        Ret = AdditionOfDigits(num)
        print("Addition of Digits in number", num, "are" , Ret)
       
    except ValueError as vobj:
        print("Please enter numeric value")
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()
