
def NumberStartingFromOne(No):
    """
    Docstring for Display Numbers from 1 to No
    
    Arguments:
    param No: Number

    Returns:
    list : Numbers from 1 to No
    """
    numbers = list()
    for i in range(1, No + 1):
        numbers.append(i)

    return numbers

def main():
    try:
        print("Enter the number")
        iNo = int(input())

        if iNo < 0:
            print("Number is not natural number")
        else:
            Ret = NumberStartingFromOne(iNo)
            for i in range(len(Ret)):
                if i == (len(Ret) - 1):
                    print(Ret[i])
                else:
                    print(Ret[i], end="\t")
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()

