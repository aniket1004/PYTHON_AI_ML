
def addition(*No):
    Ans = 0
    for N in No:
        Ans = Ans + N
    
    return Ans

def subtraction(No1, No2):
    Ans = 0
    Ans = No1 - No2
    return Ans

def multiplication(*No):
    Ans = 1
    for N in No:
        Ans = Ans * N
    
    return Ans

def division(No1, No2):
    Ans = 0
    try:
        Ans = No1 / No2
    except ZeroDivisionError as zobj:
        #print(zobj)
        Ans = "Cannot divide by 0"
    
    return Ans

def main():
    print("Enter first number:")
    No1 = int(input())

    print("Enter second number:")
    No2 = int(input())

    Ans = addition(No1, No2)
    print("Addition of numbers :", Ans)

    Ans = subtraction(No1, No2)
    print("Subtraction of numbers :", Ans)

    Ans = multiplication(No1, No2)
    print("Multiplication of numbers :", Ans)

    Ans = division(No1, No2)
    print("Division of numbers :", Ans)

if __name__ == "__main__":
    main()
    