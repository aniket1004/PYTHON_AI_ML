import threading

def Display():
    for i in range(10):
        print("inside display :", threading.get_ident())

def main():
    print("Inside Main", threading.get_ident())
    
    t1 = threading.Thread(target=Display)
    t1.start()
    
    t2 = threading.Thread(target=Display)
    t2.start()

    t1.join()
    t2.join()

    print("End Main", threading.get_ident())

if __name__ == "__main__":
    main()