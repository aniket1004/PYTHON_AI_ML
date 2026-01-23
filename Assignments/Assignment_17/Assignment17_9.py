
def CountDigitOfNumber(No):
    """
    Docstring for CountDigitOfNumber
    Accept number from user and return number of digits in that number.
    No : 5187934 
    Return Value : 7
    
    :param No: Numeric Value

    """
    count = 0
    if No == 0:
        count = 1
        return count
    
    while No > 0 :
        count = count + 1
        No = No // 10

    return count


def main():
   
    try :
        print("Enter the number:", end=" ")
        num = int(input())

        count = CountDigitOfNumber(num)
        print("Digits in number", num, "are" , count)
       
    except ValueError as vobj:
        print("Please enter numeric value")
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()
