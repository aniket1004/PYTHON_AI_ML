
"""
Docstring for LambdaCheckOdd
This lambda function accept one number and check whether number is odd or not -> (bool)
"""
CheckOdd = lambda No :  not(No % 2 == 0)

def main():
    try:
        print ("Enter the number:", end=" ")
        iNo = int(input())
        Ret = CheckOdd(iNo)
        if Ret :
            print ("Given number", iNo, "is odd")
        else:
            print ("Given number", iNo, "is not odd")
    except ValueError as vobj:
        print("Given input should be number:", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()