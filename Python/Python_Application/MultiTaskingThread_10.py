import threading

def SumEven(No):
    Sum = 0
    for i in range(2, No + 1, 2):
        Sum = Sum + i
    print("Even Sum is :", Sum)

def SumOdd(No):
    Sum = 0
    for i in range(1, No + 1, 2):
        Sum = Sum + i
    print("Odd Sum is :", Sum)

def main():
    SumEven(100000000)
    SumOdd(100000000)

if __name__ == "__main__":
    main()