import threading

def Display(No):
    print("Inside Display :", No)

def main():
    t = threading.Thread(target=Display, args=(11,))
    t.start()
    

if __name__ == "__main__":
    main()