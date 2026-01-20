
"""
Docstring for LambdaCheckDividedByFive
This lambda function accept one number and check whether number divisible by 5 or not -> (bool)
"""
DivisibleByFive = lambda No : No % 5 == 0

def main():
    try:
        print ("Enter the number:", end=" ")
        iNo = int(input())
        Ret = DivisibleByFive(iNo)
        if Ret :
            print ("Given number", iNo, "is divisible by 5")
        else:
            print ("Given number", iNo, "is not divisible by 5")
    except ValueError as vobj:
        print("Given input should be number:", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()