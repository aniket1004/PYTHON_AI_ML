
iCnt = 0
def update():
    global iCnt
    for _ in range(2000000):
        iCnt = iCnt + 1

def main():
    global iCnt
    update()
    update()
    print("Value of iCnt is", iCnt)

if __name__ == "__main__":
    main()