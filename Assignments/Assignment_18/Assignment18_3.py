import AcceptInputModule

def MinimumFromList(numbers):
    """
    Docstring for MinimumFromList
    Accept N numbers from user and store it into List. Return Minimum number from that List.
    
    :param numbers: List of numbers
    """
    Min = 0
    if numbers is None or len(numbers) == 0:
        return "No Minimum number found"
    
    Min = numbers[0]
    for i in range(1, len(numbers)):
        if (numbers[i] < Min):
            Min = numbers[i]

    return Min

def main():
    N = AcceptInputModule.AcceptNumberOfElements()
    numbers = AcceptInputModule.AcceptNumbersToStoreForList(N)

    Ret = MinimumFromList(numbers)
    print("Minimum  number from list is :", Ret)

if __name__ == "__main__":
    main()