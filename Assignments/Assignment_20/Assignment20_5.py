import threading

def one_to_fifty():
    for i in range(1, 51):
        print(i, end="  ")
    print("")

def fifty_to_one():
    for i in range(50, 0, -1):
        print(i, end="  ")
    print("")
    
def main():
    try:
        t1 = threading.Thread(target=one_to_fifty)
        t2 = threading.Thread(target=fifty_to_one)

        t1.start()
        t1.join()

        t2.start()
        t2.join()
        
    except Exception as eobj:
        print(eobj)
    
if __name__ == "__main__":
    main()

