
def OddNumberTillNumber(No):
    """
    Docstring for Odd Numbers Till given Number
    
    Arguments
    :param No: Number

    Returns
    OddNumbers -> list (list contains all odd numbers till numbers)
    """
    OddNumbers = list()

    for i in range(1, No + 1):
        if i % 2 != 0:
            OddNumbers.append(i)
    
    return OddNumbers

def main():
    try:
        print("Enter the number")
        iNo = int(input())

        if iNo < 0:
            print("Number is not natural number")
        else:
            OddNumbers = OddNumberTillNumber(iNo)
            if OddNumbers is not None and len(OddNumbers) > 0:
                for i in range(len(OddNumbers)):
                    if i == (len(OddNumbers)-1):
                        print(OddNumbers[i])
                    else:
                        print(OddNumbers[i], end="\t")
            else:
                print("Odd number not found")
            
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()