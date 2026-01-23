
def ChkNum(No):
    """
    Docstring for function ChkNum

    Check whether that number is positive or negative or zero.

    Arguments
    :param No: Number as int 

    Returns
    str : Message String
    """
    # if No == 0:
    #     print("Zero")
    # elif No > 0:
    #     print("Positive Number")
    # elif No < 0:
    #     print("Negative Number")
    return ("Zero" if No == 0 else ("Positive Number" if No > 0 else "Negative Number"))

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