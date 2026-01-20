
"""
Docstring for LambdaSquare
This Lambda function accept one number and return square of that number.
"""
Square = lambda No : No**2

def main():
    try:
        print ("Enter the number:", end=" ")
        iNo = int(input())
        Ret = Square(iNo)
        print("Square of given number", iNo, "is :", Ret)
    except ValueError as vobj:
        print("Given input should be number:", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()