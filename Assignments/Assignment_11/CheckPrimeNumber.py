
def CheckPrime(No):
    """
    Docstring for CheckPrime
    Greater than 1
    number which are divisible by only [1 and number itself].
    
    Arguments
    :param No: Number

    Returns
    isPrime -> bool (Return prime number or not)
    """
    isPrime = False
    for i in range(2, No + 1):
        if i == No:
            isPrime = True
            break
        else:
            if No % i == 0:
                isPrime = False
                break
    
    return isPrime

def main():
    try:
        print("Enter the number")
        iNo = int(input())

        if iNo <= 1:
            print("Number should not be less than equal to 1")
        else:
            Ret = CheckPrime(iNo)
            if Ret:
                print("Given number", iNo, "is: Prime number")
            else:
                print("Given number", iNo, "is: Not prime number")
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()