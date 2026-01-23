
def Add(No1, No2):
    Ret = 0
    Ret = No1 + No2
    return Ret

def Sub(No1, No2):
    Ret = 0
    Ret = No1 - No2
    return Ret

def Mult(No1, No2):
    Ret = 0
    Ret = No1 * No2
    return Ret

def Div(No1, No2):
    Ret = 0
    if No2 == 0:
        return "Cannot Divided by 0"
    Ret = No1 / No2

    return Ret