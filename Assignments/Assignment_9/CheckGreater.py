
def CheckGreater(No1, No2):
    """
    Function CheckGreater accepts two numbers and returns greater number
    
    Args:
    param No1: First Number (int, float)
    param No2: Second Number (int, float)

    Returns:
        Greater Number (int, float)

    """
    if No1 > No2 :
        return No1
    else :
        return No2

def main():
    print("Please enter first number :")
    Number1 = int(input())
    print("Please enter second number :")
    Number2 = int(input())

    GreaterNumber = CheckGreater(No1=Number1, No2= Number2)
    print(GreaterNumber, "is greater")

if __name__ == "__main__":
    main()
    