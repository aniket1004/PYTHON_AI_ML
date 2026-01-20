"""
    DocString for LambdaSquares
    This program accepts list of numbers and return list of squares of each number.
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
        
        Result = list(map(lambda N : N ** 2, Numbers))
        for i in range(len(Result)):
            print("Square of number",Numbers[i], "is :", Result[i])

    except ValueError as vobj:
        print("Value should be number :", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()