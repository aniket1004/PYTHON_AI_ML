
def NumberInReverseOrder(No):
    """
    Docstring for Display Numbers No to 1
    
    Arguments:
    param No: Number

    Returns:
    list : Numbers from No to 1
    """
    numbers = list()
    for i in range(No, 0, -1):
        numbers.append(i)

    return numbers

def main():
    try:
        print("Enter the number")
        iNo = int(input())

        if iNo < 0:
            print("Number is not natural number")
        else:
            Ret = NumberInReverseOrder(iNo)
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

