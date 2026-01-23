from functools import reduce
import AcceptInputModule
"""
Docstring for filter, map , reduce
    Filter should filter out all such numbers which are even. Map function will calculate its square.
    Reduce will return addition of all that numbers.
"""

Even = lambda No : No % 2 == 0
Square = lambda No : No ** 2
Add = lambda No1, No2 : No1 + No2

def main():
    try:
        N = AcceptInputModule.AcceptNumberOfElements()
        numbers = AcceptInputModule.AcceptNumbersToStoreForList(N)

        even_list = list(filter(Even, numbers))
        square_list = list(map(Square, even_list))
        addition = 0
        if square_list is not None and len(square_list) > 0:
            addition = reduce(Add, square_list)

        print("Final output of the reduce is:", addition)
        
    except ValueError as vobj:
        print("Input value should be numeric")
    except Exception as eobj:
        print(eobj)
    
if __name__ == "__main__":
    main()