"""
    DocString for LambdaFindOdd
    This program accepts list of numbers and return list of odd numbers from list.
"""

def main():
    try:
        print("How many numbers:", end=" ")
        Size = int(input())
        Numbers = list()
        for i in range(Size):
            print("Enter number:", end=" ")
            No = int (input())
            Numbers.append(No)
        
        Result = list(filter(lambda N : N % 2 != 0, Numbers))
        print("Odd numbers from given list are:")
        print(Result)

    except ValueError as vobj:
        print("Value should be number :", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()