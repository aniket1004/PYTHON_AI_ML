
def EvenNumberTillNumber(No):
    """
    Docstring for Even Number Till Number
    
    Arguments
    :param No: Number

    Returns
    EvenNumbers -> list (list contains all even numbers till numbers)
    """
    EvenNumbers = list()

    for i in range(2, No + 1):
        if i % 2 == 0:
            EvenNumbers.append(i)
    
    return EvenNumbers

def main():
    try:
        print("Enter the number")
        iNo = int(input())

        if iNo < 0:
            print("Number is not natural number")
        else:
            EvenNumbers = EvenNumberTillNumber(iNo)
            if EvenNumbers is not None and len(EvenNumbers) > 0:
                for i in range(len(EvenNumbers)):
                    if i == (len(EvenNumbers)-1):
                        print(EvenNumbers[i])
                    else:
                        print(EvenNumbers[i], end="\t")
            else:
                print("Even number not found")
            
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()