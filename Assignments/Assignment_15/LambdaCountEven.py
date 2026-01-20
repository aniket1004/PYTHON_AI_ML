"""
    DocString for LambdaCountEven
    This program accepts list of numbers and return count of even numbers from list.
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
        
        Result = list(filter(lambda N : N % 2 == 0, Numbers))
        if Result is None or len(Result) == 0:
            print("No even numbers found in given list" )
        else:
            print("Count of Even numbers from given list is :", len(Result))

    except ValueError as vobj:
        print("Value should be number :", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()