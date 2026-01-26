import sys

def main():
    Sum = 0
    
    if len(sys.argv) >= 2:
        for i in range(1, len(sys.argv)):
            Sum += int(sys.argv[i])

    print(Sum)

if __name__ == "__main__":
    main()