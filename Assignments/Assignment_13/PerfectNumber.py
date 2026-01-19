

def IsPerfectNumber(No):
    """
    Docstring for Number is perfect or not
    
    Arguments:
    param No: int

    Returns:
    perfect : True or False (bool)
    """
    perfect = False
    Sum = 0
    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    if Sum == No:
        perfect = True

    return perfect

def main():
    try:
        print("Enter the number:")
        No = int(input())

        if No <= 0:
            print("Values should be greater than 0")
        else:
            Ret = IsPerfectNumber(No)
            if Ret:
                print("Perfect Number")
            else :
                print("Not perfect number")
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()

