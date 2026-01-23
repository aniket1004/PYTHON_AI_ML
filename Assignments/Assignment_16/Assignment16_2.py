
def ChkNum(No):
    """
    Docstring for function ChkNum

    If number is even then it should display “Even number” otherwise display “Odd number” on console.

    Arguments
    :param No: Number as int 

    Returns
    str : Message String
    """
    if No % 2 == 0:
        return "Even Number"
    
    return "Odd Number"

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