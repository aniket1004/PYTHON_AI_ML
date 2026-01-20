"""
    DocString for LambdaReduceMinNumber
    This program accepts list of numbers and return minimum number from list.
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
        
        Result = reduce(lambda No1, No2 : No1 if No1 < No2 else No2, Numbers)
        print("Minimum number from list is :", Result)

    except ValueError as vobj:
        print("Value should be number :", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()