import AcceptInputModule

def MaximumFromList(numbers):
    """
    Docstring for MaximumFromList
    Accept N numbers from user and store it into List. Return Maximum number from that List.

    :param numbers: List of numbers
    """
    Max = 0
    if numbers is None or len(numbers) == 0:
        return "No maximum number found"
    
    Max = numbers[0]
    for i in range(1, len(numbers)):
        if (numbers[i] > Max):
            Max = numbers[i]

    return Max    

def main():
    N = AcceptInputModule.AcceptNumberOfElements()
    numbers = AcceptInputModule.AcceptNumbersToStoreForList(N)

    Ret = MaximumFromList(numbers)
    print("Maximum  number from list is :", Ret)

if __name__ == "__main__":
    main()