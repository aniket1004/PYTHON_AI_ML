import hashlib

def CalculateChecksum(FileName):
    fobj = open(FileName, "rb")
    
    hobj = hashlib.md5()
    
    Buffer = fobj.read(1024)

    while len(Buffer) > 0:
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    
    fobj.close()

    return hobj.hexdigest()

def main():
    Ret = CalculateChecksum("Hello.txt")
    print("Checksum is : ", Ret)

if __name__ == "__main__":
    main()