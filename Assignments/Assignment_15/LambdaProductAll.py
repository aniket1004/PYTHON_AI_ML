"""
    DocString for LambdaProductAll
    This program accepts list of numbers and return product of all numbers from list.
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
        
        Result = reduce(lambda No1, No2 : No1 * No2, Numbers)
        print("Product of all numbers from list is :", Result)

    except ValueError as vobj:
        print("Value should be number :", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()