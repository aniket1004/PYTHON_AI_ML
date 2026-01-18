
def IsDivisibleByThreeAndFive(No):
    """
    This function is check whether number is divisible by 3 and 5.
    
    Args:
    param No: Number (int, float)

    Return:
        bool : True or False
    """
    return (No % 3 == 0 and No % 5 == 0)

def main():
    print("Please enter number :")
    Number = int(input())

    if (IsDivisibleByThreeAndFive(Number)):
        print(Number, "is divisible by 3 and 5")
    else :
        print(Number, "is not divisible by 3 and 5")
    
if __name__ == "__main__":
    main()