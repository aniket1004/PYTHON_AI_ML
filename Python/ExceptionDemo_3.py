def main():
    Ans = 0
    try:
        print("Inside try")

        print("Enter first number:")
        No1 = int(input())

        print("Enter second number:")
        No2 = int(input())

        Ans = No1 / No2

    except ZeroDivisionError as zobj:
        print("Inside Except:", zobj)
    except ValueError as vobj:
        print("Inside Except:", vobj)
    except Exception as eobj:
        print("Inside Except:", eobj)
    finally:
        print("Inside Finally")
    
    print("Division is:", Ans)

if __name__ == "__main__":
    main()