from functools import reduce
CheckEven = lambda No : No % 2 == 0
Increment = lambda No : No + 1
Addition = lambda No1, No2 : No1 + No2

def filterX(Task, Elements):
    Result = list()
    for No in Elements:
        Ret = Task(No)
        if Ret:
            Result.append(No)
    
    return Result

def main():
    Data = [11, 10, 15, 20, 22, 27, 30]
    print ("Actual Data is :", Data)
    FData = list(filterX(CheckEven, Data))
    print("Data after filter is:", FData)

    MData = list(map(Increment, FData))
    print("Data after map is:", MData)

    RData = reduce((lambda No1, No2 : No1 + No2), MData)
    print("Data after reduce is :", RData)

if __name__ == "__main__":
    main()