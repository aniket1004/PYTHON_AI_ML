import threading

def uppercase_count(string):
    count = 0
    for str in string:
        if ord(str) >= 65 and ord(str) <= 90:   # A Z
            count += 1
    print("Uppercase letters count is:", count)
    print("Thread ID Uppercase_count:", threading.get_ident(), "| Thread Name Uppercase_count:", threading.current_thread().name)

def lowercase_count(string):
    count = 0
    for str in string:
        if ord(str) >= 97 and ord(str) <= 122:  # a z
            count += 1
    print("Lowercase letters count is:", count)
    print("Thread ID Lowercase_count:", threading.get_ident(), "| Thread Name Lowercase_count:", threading.current_thread().name)

def digit_count(string):
    count = 0
    numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
    for str in string:
        if str in numbers:
            count += 1
    print("Digit count is:", count)
    print("Thread ID Digit_count:", threading.get_ident(), "| Thread Name Digit_count:", threading.current_thread().name)
def main():
    try:
        print("Enter the string:", end=" ")
        string = input()
        
        t1 = threading.Thread(target=lowercase_count, args=(string,))
        t2 = threading.Thread(target=uppercase_count, args=(string,))
        t3 = threading.Thread(target=digit_count, args=(string,))

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()

    except Exception as eobj:
        print(eobj)
    
if __name__ == "__main__":
    main()

