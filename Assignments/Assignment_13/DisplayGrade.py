
def DisplayGrade(No):

    if No >= 75:
        print("Distinction")
    elif No >= 60:
        print("First Class")
    elif No >= 50:
        print("Second Class")
    elif No < 50:
        print("Fail")

def main():
    try:
        print("Enter the marks:")
        No = float(input())

        if No < 0:
            print("Values should be positive")
        else:
            DisplayGrade(No)
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()