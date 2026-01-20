"""
    DocString for LambdaAddAll
    This program accepts list of numbers and return sum of all numbers from list.
"""
from functools import reduce

def main():
    try:
        print("How many numbers:", end=" ")
        Size = int(input())
        Numbers = list()
        for i in range(Size):
            print("Enter number:", end=" ")
            No = int (input())
            Numbers.append(No)
        
        Ret = reduce(lambda No1, No2 : No1 + No2, Numbers)
        print("Addition of all numbers from list is :", Ret)

    except ValueError as vobj:
        print("Value should be number :", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()