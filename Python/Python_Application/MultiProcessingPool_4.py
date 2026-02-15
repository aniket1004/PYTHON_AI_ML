import time
import multiprocessing

def SumCube(No):
    Sum = 0
    for i in range(1, No + 1):
        Sum = Sum + (i ** 3)

    return Sum

def main():
    Data = [1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,1000000]
    Result = list()

    start_time = time.time()
    
    pobj = multiprocessing.Pool()
    Result = pobj.map(SumCube, Data)

    pobj.close()
    pobj.join()
    
    end_time = time.time()

    print(Result)
    print("Required Time for execution :", end_time - start_time, "seconds")
    # 1.5491230487823486 seconds

if __name__ == "__main__":
    main()