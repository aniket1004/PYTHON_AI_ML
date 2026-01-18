import threading

def Display():
    print("Inside Display Function ", threading.get_ident())

def main():
    print("Inside Main", threading.get_ident())
    t = threading.Thread(target=Display)
    t.start()
    print("End Main", threading.get_ident())

if __name__ == "__main__":
    main()