
def Cube(No):
    """
    Function accept one number and return cube of that number 
    
    Args:
    param No: Number (int, float)

    Returns:
        Number (int, float)
    """
    Ans = No**3

    return Ans

def main():
    print("Please enter number :")
    Number = int(input())

    Result = Cube(Number)
    print("Cube of given number is:", Result)

if __name__ == "__main__":
    main()
