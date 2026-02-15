
def CheckEven(No):
    return (No % 2 == 0)

def main():
    Data = [11, 10, 15, 20, 22, 27, 30]
    print ("Actual Data is :", Data)
    FData = list(filter(CheckEven, Data))
    print("Data after filter is:", FData)

    

if __name__ == "__main__":
    main()