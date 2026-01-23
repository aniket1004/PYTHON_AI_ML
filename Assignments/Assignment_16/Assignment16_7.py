
def ChkNum(No):
    """
    Docstring for function ChkNumDivisibleByFive

    Check whether that number is Divisible By Five.

    Arguments
    :param No: Number as int 

    Returns
    bool : True if divisible by 5 else False
    """
    if No == None:
        return False
    
    return No % 5 == 0

def main():
    try:
        print("Enter the number:", end=" ")
        Number = int(input())
        Result = ChkNum(Number)
        print(Result)
    except ValueError as vobj:
        print("Please enter numeric value =>", vobj)
    except Exception as eobj:
        print(eobj)
    

if __name__ == "__main__":
    main()