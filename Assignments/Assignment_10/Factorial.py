
def Factorial(No):
    """
    Docstring for Factorial
    
    Arguments
    :param No: Number

    Returns
    Fact -> int (Factorial of given number)
    """
    Fact = 1
    for i in range(2, No + 1):
        Fact = Fact * i

    return Fact

def main():
    try:
        print("Enter the number")
        iNo = int(input())

        if iNo < 0:
            print("Number is not natural number")
        else:
            Ret = Factorial(iNo)
            print("Factorial of given number", iNo, "is ", Ret)
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()