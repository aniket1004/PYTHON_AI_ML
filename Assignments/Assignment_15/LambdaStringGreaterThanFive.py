"""
    DocString for LambdaStringGreaterThanFive
    This program accepts list of strings and return strings having length greater than 5 from list.
"""

def main():
    try:
        print("How many strings:", end=" ")
        Size = int(input())
        Strings = list()
        for i in range(Size):
            print("Enter string:", end=" ")
            String = input()
            Strings.append(String)
        
        Result = list(filter(lambda str : (str is not None and len(str) > 5), Strings))
        print("String having length greater than five are :")
        for String in Result:
            print(String)

    except ValueError as vobj:
        print("Value should be number :", vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()