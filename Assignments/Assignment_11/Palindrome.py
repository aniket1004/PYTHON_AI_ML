import ReverseNumber

def IsPalindrome(No):
    """
    Docstring for IsPalindrome
    
    Arguments:
    param No: Number

    Returns:
    Ret : Number is palindrome or not (bool)
    """
    Ret = False
    ReverseNum = ReverseNumber.ReverseTheNumber(No)
    if No == ReverseNum:
        Ret = True
    else :
        Ret = False

    return Ret

def main():
    try:
        print("Enter the number")
        iNo = int(input())

        if iNo < 0:
            print("Number is not natural number")
        else:
            Ret = IsPalindrome(iNo)
            if Ret :
                print("Palindrome")
            else:
                print("Not palindrome")
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()

