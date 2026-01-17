from functools import reduce

def main():
    Data = [11, 10, 15, 20, 22, 27, 30]
    print ("Actual Data is :", Data)
    FData = list(filter((lambda No : No % 2 == 0), Data))
    print("Data after filter is:", FData)

    MData = list(map((lambda No : No + 1), FData))
    print("Data after map is:", MData)

    RData = reduce((lambda No1, No2 : No1 + No2), MData)
    print("Data after reduce is :", RData)

if __name__ == "__main__":
    main()