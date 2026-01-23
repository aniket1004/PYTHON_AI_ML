import Arithmetic

def main():
    """
    Docstring for main
        1.Create on module named as Arithmetic which contains 4 functions as Add()
        for addition, Sub()
        for subtraction, Mult() for multiplication and Div() for division. All functions
        accepts two
        parameters as number and perform the operation. Write on python program
        which call all the
        functions from Arithmetic module by accepting the parameters from user.
    """
    try:
        
        print ("Enter the first number:", end=" ")
        No1 = int(input())

        print ("Enter the second number:", end=" ")
        No2 = int(input())

        Ret = Arithmetic.Add(No1, No2)
        print("Addition of given numbers is:", Ret)

        Ret = Arithmetic.Sub(No1, No2)
        print("Subtraction of given numbers is:", Ret)

        Ret = Arithmetic.Mult(No1, No2)
        print("Multiplication of given numbers is:", Ret)

        Ret = Arithmetic.Div(No1, No2)
        print("Division of given numbers is:", Ret)



    except ValueError as vobj:
        print("Please enter valid number", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()