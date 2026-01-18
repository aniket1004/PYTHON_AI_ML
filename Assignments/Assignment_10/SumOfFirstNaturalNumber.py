
def SumOfNaturalNumber(No):
    """
    Docstring for SumOfNaturalNumber
    
    Arguments:
    param No: Natural Number

    Returns:
    Sum : Summation First N natural number (int)
    """
    Sum = 0
    for i in range(1, No + 1):
        Sum = Sum + i

    return Sum

def main():
    try:
        print("Enter the number")
        iNo = int(input())

        if iNo < 0:
            print("Number is not natural number")
        else:
            Ret = SumOfNaturalNumber(iNo)
            print("Summation of first", iNo, "natural numbers:", Ret)
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()

