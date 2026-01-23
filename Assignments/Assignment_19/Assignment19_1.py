
"""
Docstring for Lambda Square
    Program contains one lambda function which accepts one parameter and return power of two.
"""
Square = lambda No : No ** 2

def main():
    try:
        print("Enter the number:", end=" ")
        No = int(input())
        Ret = Square(No)
        print("Power of two for given number is:", Ret)
    except ValueError as vobj:
        print("Input value should be numeric")
    except Exception as eobj:
        print(eobj)
    
if __name__ == "__main__":
    main()