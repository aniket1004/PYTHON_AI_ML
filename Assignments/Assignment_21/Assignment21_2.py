import AcceptInputModule
import threading

def Maximum(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    print("Maximum number from list is:", max)

def Minimum(numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    print("Minimum number from list is:", min)


def main():
    N = AcceptInputModule.AcceptNumberOfElements()
    numbers = AcceptInputModule.AcceptNumbersToStoreForList(N)
    
    t1 = threading.Thread(target=Maximum, args=(numbers,))
    t2 = threading.Thread(target=Minimum, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()