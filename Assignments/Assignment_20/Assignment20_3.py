import threading
import AcceptInputModule

def EvenList(Elements):
    Sum = 0
    for No in Elements:
        if No % 2 == 0:
            Sum += No

    print("Sum of even numbers from list is:", Sum)

def OddList(Elements):
    Sum = 0
    for No in Elements:
        if No % 2 != 0:
            Sum += No
    
    print("Sum of odd numbers from list is:", Sum)

def main():
    try:
        N = AcceptInputModule.AcceptNumberOfElements()
        elements = AcceptInputModule.AcceptNumbersToStoreForList(N)

        t1 = threading.Thread(target=EvenList, args=(elements,))
        t2 = threading.Thread(target=OddList, args=(elements,))

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

