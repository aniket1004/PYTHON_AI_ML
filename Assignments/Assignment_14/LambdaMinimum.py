
"""
Docstring for LambdaMinimum
This Lambda function accept two numbers and return minimum number.
"""
Minimum = lambda No1, No2 : No1 if No1 < No2 else No2

def main():
    try:
        print ("Enter the first number:", end=" ")
        iNo1 = int(input())
        print ("Enter the second number:", end=" ")
        iNo2 = int(input())

        Ret = Minimum(iNo1, iNo2)
        print("Minimum number from given number is:", Ret)
    except ValueError as vobj:
        print("Given input should be number:", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()