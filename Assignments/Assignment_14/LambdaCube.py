
"""
Docstring for LambdaCube
This Lambda function accept one number and return cube of that number.
"""
Cube = lambda No : No**3

def main():
    try:
        print ("Enter the number:", end=" ")
        iNo = int(input())
        Ret = Cube(iNo)
        print("Cube of given number", iNo, "is :", Ret)
    except ValueError as vobj:
        print("Given input should be number:", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()