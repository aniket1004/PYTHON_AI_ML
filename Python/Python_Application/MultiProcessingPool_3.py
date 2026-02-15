import time
import os

def SumCube(No):
    print("Process is running with PID :", os.getpid())
    Sum = 0
    for i in range(1, No + 1):
        Sum = Sum + (i ** 3)

    return Sum

def main():
    Data = [1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,1000000]
    Result = list()

    start_time = time.time()
    
    for i in range(len(Data)):
        Ret = SumCube(Data[i])
        Result.append(Ret)
    
    end_time = time.time()

    print(Result)
    print("Required Time for execution :", end_time - start_time, "seconds")
    # 4.141597032546997 seconds 

if __name__ == "__main__":
    main()