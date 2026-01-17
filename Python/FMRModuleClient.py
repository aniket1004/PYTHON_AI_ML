from MarvellousFMR import filterX
from MarvellousFMR import mapX
from MarvellousFMR import reduceX

CheckEven = lambda No : No % 2 == 0
Increment = lambda No : No + 1
Addition = lambda No1, No2 : No1 + No2

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