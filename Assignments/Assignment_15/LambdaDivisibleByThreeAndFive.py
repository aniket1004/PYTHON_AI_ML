"""
    DocString for LambdaDivisibleByThreeAndFive
    This program accepts list of numbers and return list of numbers which is divisible by both 3 and 5.
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
        
        Result = list(filter(lambda N : (N % 3 == 0 and N % 5 == 0), Numbers))
        print("Numbers which is divisible by 3 and 5 from given list are:")
        print(Result)

    except ValueError as vobj:
        print("Value should be number :", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()