import AcceptInputModule

def FrequencyOfNumberFromList(numbers, search):
    """
    Docstring for FrequencyOfNumberFromList
    Accept N numbers from user and store it into List. 
    Accept one another number from user and return frequency of that number from List.
    
    :param numbers: List of numbers
    """
    count = 0

    for i in range(len(numbers)):
        if numbers[i] == search:
            count += 1
    
    return count

def main():
    N = AcceptInputModule.AcceptNumberOfElements()
    numbers = AcceptInputModule.AcceptNumbersToStoreForList(N)

    try:
        print("Enter the number that you want search :", end=" ")
        search = int(input())

        Ret = FrequencyOfNumberFromList(numbers, search)

        print("Frequency of the given number from the list is :", Ret)
    except ValueError as vobj:
        print("Please enter numeric value in search")
    except Exception as eobj:
        print(eobj)
if __name__ == "__main__":
    main()