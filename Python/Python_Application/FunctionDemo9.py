# One function can call another function

def fun():
    print ("Inside Fun")

def gun():
    print ("Inside Gun")

def main():
    fun()
    gun()

if __name__ == "__main__":
    main()