
def factors_addition(No):
    """
    Docstring for factors_addition
    Accept one number form user and return addition of its factors.
    
    :param No: Numeric value

    """
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    return Sum

def main():
   
    try :
        print("Enter the number:", end=" ")
        num = int(input())

        Ret = factors_addition(num)
        print("Addition of factors for given number :", Ret)

    except ValueError as vobj:
        print("Please enter numeric value")
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()
