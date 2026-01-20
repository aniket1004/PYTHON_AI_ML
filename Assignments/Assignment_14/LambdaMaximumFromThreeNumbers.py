
"""
Docstring for LambdaMaximumFromThreeNumbers
This Lambda function accept three numbers and return maximum number.
"""
Maximum = lambda No1, No2, No3 : No1 if (No1 > No2 and No1 > No3) else (No2 if ( No2 > No3) else No3)

def main():
    try:
        print ("Enter the first number:", end=" ")
        iNo1 = int(input())
        print ("Enter the second number:", end=" ")
        iNo2 = int(input())
        print ("Enter the third number:", end=" ")
        iNo3 = int(input())

        Ret = Maximum(iNo1, iNo2, iNo3)
        print("Maximum number from given number is:", Ret)
    except ValueError as vobj:
        print("Given input should be number:", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()