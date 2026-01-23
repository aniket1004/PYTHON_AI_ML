

def IsPrime(No):
    prime_number = False

    for i in range(2, No + 1):
        if i == No:
            prime_number = True
            break
        else:
            if No % i == 0:
                prime_number = False
                break

    return prime_number

def main():
   
    try :
        print("Enter the number:", end=" ")
        num = int(input())

        Ret = IsPrime(num)
        if Ret:
            print("Prime number")
        else :
            print("Not prime number")

    except ValueError as vobj:
        print("Please enter numeric value")
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()
