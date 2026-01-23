import AcceptInputModule
import MarvellousNum

addition = lambda No1, No2 : No1 + No2

def ListPrime(numbers):
    """
    Docstring for ListPrime
    Accept N numbers from user and store it into List. Return addition of all prime numbers from that List. 
    
    Main python file accepts N numbers from user and pass each number to ChkPrime() function 
    which is part of our user defined module named as MarvellousNum. 
    Name of the function from main python file should be ListPrime().

    """
    prime_list = list()

    if len(numbers) > 0:
        prime_list = list(filter(MarvellousNum.ChkPrime, numbers))
    
    return prime_list

def AdditionOfPrime(prime_numbers):
    Sum = 0

    if prime_numbers is not None and len(prime_numbers) > 0:
        for number in prime_numbers:
            Sum += number

    return Sum

def main():
    N = AcceptInputModule.AcceptNumberOfElements()
    numbers = AcceptInputModule.AcceptNumbersToStoreForList(N)

    try:
        prime_numbers = ListPrime(numbers)
        Result = 0
        
        if prime_numbers is not None and len(prime_numbers) > 0:
            Result = AdditionOfPrime(prime_numbers)

        print("Addition of pime numbers is : ", Result)

    except ValueError as vobj:
        print("Please enter numeric value in search")
    except Exception as eobj:
        print(eobj)
if __name__ == "__main__":
    main()