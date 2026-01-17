
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

def mapX(Task, Elements):
    Result = list()
    for No in Elements:
        Ret = Task(No)
        Result.append(Ret)
    
    return Result

def reduceX(Task, Elements):
    if len(Elements) == 0:
        return None
    
    Result = Elements[0]
    for i in range(1, len(Elements)):
        Result = Task(Result, Elements[i])
    
    return Result

def main():
    Data = [11, 10, 15, 20, 22, 27, 30]
    print ("Actual Data is :", Data)
    FData = list(filterX(CheckEven, Data))
    print("Data after filter is:", FData)

    MData = list(mapX(Increment, FData))
    print("Data after map is:", MData)

    RData = reduceX((lambda No1, No2 : No1 + No2), MData)
    print("Data after reduce is :", RData)

if __name__ == "__main__":
    main()