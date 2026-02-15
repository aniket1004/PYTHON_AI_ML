# Procedural Approach

def CheckEven(No):
    if (No % 2 == 0):
        print(No, " Even Number", sep=":")
    else:
        print(No, " Odd Number", sep=":")

Value = 0

print("Enter number", end= "\t")
Value = int(input())
CheckEven(Value)
