import AcceptInputModule
from functools import reduce

add = lambda No1, No2 : No1 + No2

def main():
    """
    Docstring for main
    Accept N numbers from user and store it into List. Return addition of all elements from that List.
    """
    total_numbers = AcceptInputModule.AcceptNumberOfElements()
    numbers = AcceptInputModule.AcceptNumbersToStoreForList(total_numbers)
    
    addition = reduce(add, numbers)
    print("Addition of all elements from list is :", addition)

if __name__ == "__main__":
    main()