
def Square(No):
    """
    Function accept one number and return square of that number 
    
    Args:
    param No: Number (int, float)

    Returns:
        Number (int, float)
    """
    Ans = No**2

    return Ans

def main():
    print("Please enter number :")
    Number = int(input())

    Result = Square(Number)
    print("Square of given number is:", Result)

if __name__ == "__main__":
    main()
