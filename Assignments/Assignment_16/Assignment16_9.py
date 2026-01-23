
def GetFirstNEvenNumbers(No):
    """
    Docstring for function GetFirstNEvenNumbers

    Return the display first No even numbers.

    Arguments
    :param No: Number as int 

    Returns
    list : First N Even numbers
    """
    even_numbers = list()

    for i in range(2, (No * 2) + 1, 2):
        even_numbers.append(i)
    
    return even_numbers

def main():
    try:
        print("Enter the number:", end=" ")
        Number = int(input())
        
        Result = GetFirstNEvenNumbers(Number)
        if Result is not None and len(Result) > 0 :
            for R in Result:
                print(R, end="  ")
        else:
            print("No even number found")
    except ValueError as vobj:
        print("Please enter numeric value =>", vobj)
    except Exception as eobj:
        print(eobj)
    

if __name__ == "__main__":
    main()