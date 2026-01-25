import threading

counter = 0
lobj = threading.Lock()

def Increment():
    global counter
    for _ in range(2000000):
        with lobj:
            counter = counter + 1

def main():
    global counter

    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)
    t3 = threading.Thread(target=Increment)
    t4 = threading.Thread(target=Increment)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("Final value of the counter after all threads is:", counter)

if __name__ == "__main__":
    main()

