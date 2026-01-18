
def SumOfDigitsInNumber(No):
    """
    Docstring for Sum Of Digits in Number
    
    Arguments:
    param No: Number

    Returns:
    Sum : Summation of digit in number (int)
    """
    Sum = 0
    while No > 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    try:
        print("Enter the number")
        iNo = int(input())

        if iNo < 0:
            print("Number is not natural number")
        else:
            Ret = SumOfDigitsInNumber(iNo)
            print("Summation of digits in ", iNo, "is:", Ret)
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()

