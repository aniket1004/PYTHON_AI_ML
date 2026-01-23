
def Add(No1, No2):
    """
    Docstring for function Add

    This function accepts two numbers and return addition of that two numbers.

    Arguments
    :param No1: First Number
    :param No2: Second Number

    Returns
    Sum : Addition of two numbers
    """
    Sum = 0
    Sum = No1 + No2

    return Sum

def main():
    try:
        Result = 0
        print("Enter the first number:", end=" ")
        Number1 = int(input())
        print("Enter the second number:", end=" ")
        Number2 = int(input())

        Result = Add(No1=Number1, No2=Number2)
        print("Addition of two numbers is:", Result)
    except ValueError as vobj:
        print("Please enter numeric value =>", vobj)
    except Exception as eobj:
        print(eobj)
    

if __name__ == "__main__":
    main()