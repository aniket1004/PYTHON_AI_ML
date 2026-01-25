import threading

def EvenFactor(No):
    Sum = 0
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            Sum += i
    print("Sum of even factor of given number", No, "is:", Sum)

def OddFactor(No):
    Sum = 0
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            Sum += i
    
    print("Sum of odd factor of given number", No, "is:", Sum)

def main():
    try:
        print("Enter the number:", end=" ")
        No = int(input())

        t1 = threading.Thread(target=EvenFactor, args=(No,))
        t2 = threading.Thread(target=OddFactor, args=(No,))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print("Exit from main")

    except ValueError as vobj:
        print("Input value should be numeric")
    except Exception as eobj:
        print(eobj)
    
if __name__ == "__main__":
    main()

