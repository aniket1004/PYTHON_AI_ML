
def ReverseTheNumber(No):
    """
    Docstring for Reverse the Number
    
    Arguments:
    param No: Number

    Returns:
    ReverseNum : Reverse number (int)
    """
    ReverseNum = 0
    while No > 0:
        Digit = No % 10
        ReverseNum = (ReverseNum * 10) + Digit
        No = No // 10

    return ReverseNum

def main():
    try:
        print("Enter the number")
        iNo = int(input())

        if iNo < 0:
            print("Number is not natural number")
        else:
            Ret = ReverseTheNumber(iNo)
            print("Reverse number of", iNo, "is:", Ret)
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()

