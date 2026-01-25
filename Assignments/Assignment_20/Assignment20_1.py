import threading

def DisplayEven(No):
    for i in range(2, (No * 2) + 1, 2):
        print("Even Number:", i)

def DisplayOdd(No):
    for i in range(1, (No * 2) + 1, 2):
        print("Odd Number:", i)

def main():
    print("How many N numbers:", end=" ")
    N = int(input())

    thread1 = threading.Thread(target=DisplayEven, args=(N,))
    thread2 = threading.Thread(target=DisplayOdd, args=(N,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()

