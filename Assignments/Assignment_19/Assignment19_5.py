from functools import reduce
import AcceptInputModule
"""
Docstring for filter, map , reduce
    Filter should filter out all prime numbers. Map function will multiply each number by 2. 
    Reduce will return Maximum number from that numbers.
"""

def ChkPrime(No):
    is_prime = False
    for i in range(2, No + 1):
        if i == No:
            is_prime = True
            break
        else:
            if No % i == 0:
                is_prime = False
                break
    return is_prime

def MultiplyByTwo(No):
    Ans = 0
    Ans = No * 2
    return Ans

def Maximum(No1, No2):
    return (No1 if No1 > No2 else No2)


def main():
    try:
        N = AcceptInputModule.AcceptNumberOfElements()
        numbers = AcceptInputModule.AcceptNumbersToStoreForList(N)

        prime_list = list(filter(ChkPrime, numbers))
        multiply_list = list(map(MultiplyByTwo, prime_list))
        maximum = 0
        if multiply_list is not None and len(multiply_list) > 0:
            maximum = reduce(Maximum, multiply_list)

        print("Final output of the reduce is:", maximum)
        
    except ValueError as vobj:
        print("Input value should be numeric")
    except Exception as eobj:
        print(eobj)
    
if __name__ == "__main__":
    main()