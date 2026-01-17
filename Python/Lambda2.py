# Functional Approach

# def CheckEven(No):
#     return (No % 2 == 0)
#lambda Parameters : Body
CheckEven = lambda No : No % 2 == 0

def main():
    Value = 0
    Ret = False

    print("Enter number", end= "\t")
    Value = int(input())
    Ret = CheckEven(Value)
    if Ret:
        print(Value, "Even number")
    else:
        print(Value, "Odd Number")

if __name__ == "__main__":
    main()