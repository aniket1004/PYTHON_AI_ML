
"""
Docstring for Lambda Multiplication
    Program which contains one lambda function which accepts two parameters and return its multiplication
"""
Multiplication = lambda No1 , No2 : No1 * No2

def main():
    try:
        print("Enter the first number:", end=" ")
        No1 = int(input())

        print("Enter the second number:", end=" ")
        No2 = int(input())

        Ret = Multiplication(No1, No2)
        print("Multiplication of given numbers are:", Ret)
    except ValueError as vobj:
        print("Input value should be numeric")
    except Exception as eobj:
        print(eobj)
    
if __name__ == "__main__":
    main()