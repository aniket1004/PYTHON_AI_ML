
def PrintStars(No):
    """
    Docstring for function PrintStars

    Print given number of stars on screen.

    Arguments
    :param No: Number as int 

    Returns
    None
    """
    for _ in range(No):
        print("*", end=" ")

def main():
    try:
        print("Enter the number:", end=" ")
        Number = int(input())
        PrintStars(Number)
    except ValueError as vobj:
        print("Please enter numeric value =>", vobj)
    except Exception as eobj:
        print(eobj)
    

if __name__ == "__main__":
    main()