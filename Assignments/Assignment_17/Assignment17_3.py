
def factorial(No):
    """
    Docstring for factorial
    Accept one number from user and return its factorial.

    :param No: Numeric value
    Returns
    fact : int
    """
    fact = 1
    for i in range(2, No + 1):
        fact = fact * i

    return fact

def main():
   
    try :
        print("Enter the number:", end=" ")
        num = int(input())

        Ret = factorial(num)
        print("Factorial of given number :", Ret)

    except ValueError as vobj:
        print("Please enter numeric value")
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()