def Factors(No):
    fact = list()
    for i in range(1, No + 1):
        if No % i == 0:
            fact.append(i)
    
    return fact

def main():
    try:
        print("Enter the number")
        iNo = int(input())

        if iNo < 0:
            print("Number is not natural number")
        else:
            fact = Factors(iNo)
            if fact is None or len(fact) == 0:
                print("No factors found")
            else:
                for i in range(len(fact)):
                    if i == (len(fact)-1):
                        print(fact[i])
                    else:
                        print(fact[i], end="\t")
            
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()