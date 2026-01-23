
def ChkPrime(No):
    is_prime = False
    
    if No is None:
        return is_prime

    for i in range(2, No + 1):
        if i == No:
            is_prime = True
            break
        else:
            if No % i == 0:
                is_prime = False
                break

    return is_prime