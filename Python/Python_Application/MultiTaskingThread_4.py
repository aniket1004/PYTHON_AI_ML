import threading

def Display():
    print("Inside Display Function ", threading.get_ident())
    for i in range(100):
        print("inside display")

def main():
    print("Inside Main", threading.get_ident())
    
    t = threading.Thread(target=Display)
    t.start()
    t.join()
    
    print("End Main", threading.get_ident())

if __name__ == "__main__":
    main()