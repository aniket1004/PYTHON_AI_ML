# Global Interpreter Lock
import time
import multiprocessing
import os

def SumEven(No):
    print("PID of SumEven :", os.getpid())  #   51
    print("PPID of SumEven :", os.getppid())    # 21
    Sum = 0
    for i in range(2, No + 1, 2):
        Sum = Sum + i
    print("Even Sum is :", Sum)

def SumOdd(No):
    print("PID of SumOdd :", os.getpid())   # 101
    print("PPID of SumOdd :", os.getppid()) # 21
    Sum = 0
    for i in range(1, No + 1, 2):
        Sum = Sum + i
    print("Odd Sum is :", Sum)

def main():
    print("PID of Main :", os.getpid())     # 21
    print("PPID of Main :", os.getppid())   # CMD 11
    start_time = time.time()

    t1 = multiprocessing.Process(target=SumEven, args=(100000000,))
    t2 = multiprocessing.Process(target=SumOdd, args=(100000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()
    print("Time required :", end_time - start_time)

if __name__ == "__main__":
    main()