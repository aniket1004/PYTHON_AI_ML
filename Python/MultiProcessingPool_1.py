
def SumCube(No):
    Sum = 0
    for i in range(1, No + 1):
        Sum = Sum + (i * i * i)

    return Sum

def main():
    Ret = SumCube(10)

    print(Ret)

if __name__ == "__main__":
    main()