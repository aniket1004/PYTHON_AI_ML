
"""
Docstring for LambdaMultiplication
This Lambda function accept two numbers and return multiplication of that numbers.
"""
Multiplication = lambda No1, No2 : No1 * No2

def main():
    try:
        print ("Enter the first number:", end=" ")
        iNo1 = int(input())
        print ("Enter the second number:", end=" ")
        iNo2 = int(input())

        Ret = Multiplication(iNo1, iNo2)
        print("Multiplication of given numbers is:", Ret)
    except ValueError as vobj:
        print("Given input should be number:", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()