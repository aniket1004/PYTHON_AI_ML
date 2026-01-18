
def CountDigitOfNumber(No):
    """
    Docstring for Count Digit Of Numbers
    Greater than 0
    1234 -> 4
    45 -> 2
    (Uses // operator)
    Arguments
    :param No: Number

    Returns
    iCount -> int (No Of Digits)
    """
    if No == 0:
        return 1
    
    iCount = 0
    while No > 0 :
        iCount = iCount + 1
        No = No // 10
    
    return iCount

def main():
    try:
        print("Enter the number")
        iNo = int(input())

        if iNo < 0:
            print("Number should not be less than equal to 0")
        else:
            Ret = CountDigitOfNumber(iNo)
            print("Total digits in number", iNo, "is:", Ret)
            
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()
