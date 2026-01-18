import time

def Factorial(No):
    Fact = 1
    for i in range(1, No + 1):
        Fact = Fact * i

    return Fact

def main():
    Value = int(input("Enter the number :"))
    Start_Time = time.time()
    Ret = Factorial(Value)
    End_Time = time.time()
    print("Factorial is :", Ret)
    print("Total execution time is :", End_Time - Start_Time)

if __name__ == "__main__":
    main()