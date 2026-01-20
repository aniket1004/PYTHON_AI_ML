
"""
Docstring for LambdaCheckEven
This lambda function accept one number and check whether number is even or not -> (bool)
"""
CheckEven = lambda No : No % 2 == 0

def main():
    try:
        print ("Enter the number:", end=" ")
        iNo = int(input())
        Ret = CheckEven(iNo)
        if Ret :
            print ("Given number", iNo, "is even")
        else:
            print ("Given number", iNo, "is not even")
    except ValueError as vobj:
        print("Given input should be number:", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()