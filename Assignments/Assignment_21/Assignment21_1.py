import AcceptInputModule
import threading

def Prime(numbers):
    for i in numbers:
        for j in range(2, i + 1):
            if i == j:
                print("Prime number:", i)
            else:
                if i % j == 0:
                    break

def NonPrime(numbers):
    for i in numbers:
        for j in range(2, i):
            if i % j == 0:
                print("Non Prime number:", i)
                break


def main():
    N = AcceptInputModule.AcceptNumberOfElements()
    numbers = AcceptInputModule.AcceptNumbersToStoreForList(N)
    
    t1 = threading.Thread(target=Prime, args=(numbers,))
    t2 = threading.Thread(target=NonPrime, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()