
def MultiplicationTable(No, Stop = 10):
    """
    Docstring for MultiplicationTable
    Accepts one number and print multiplication table of that number

    Arguments:
    param No: Number (int, float)
    param Stop : Number(int) of elements of that table

    Returns :
        table -> list (contains table of that given number) 
    """
    table = list()

    for i in range(1, Stop + 1):
        Num = No * i
        table.append(Num)

    return table

def main():
    try:
        print("Enter the number:")
        iNo = int(input())

        if iNo == 0:
            print("Number should not be 0")
        else :
            table_of_no = MultiplicationTable(iNo)

            if len(table_of_no) > 0:
                for i in range(len(table_of_no)):
                    if i == (len(table_of_no) - 1):
                        print(table_of_no[i])
                    else:
                        print(table_of_no[i], end="\t")

    except ValueError as eobj:
        print(eobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()
