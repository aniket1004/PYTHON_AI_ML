# Procedural Approach

def CheckEven(No):
    if (No % 2 == 0):
        print(No, " Even Number", sep=":")
    else:
        print(No, " Odd Number", sep=":")

def main():
    CheckEven(21) # Positional Argument
    CheckEven(No = 22) # Keyword Argument

if __name__ == "__main__":
    main()