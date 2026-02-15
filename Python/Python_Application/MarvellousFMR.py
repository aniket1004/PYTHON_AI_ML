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
