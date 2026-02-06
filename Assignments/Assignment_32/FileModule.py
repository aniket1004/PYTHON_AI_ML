import os
import hashlib

def GetCheckSum(FileName):
    CheckSum = None
    hobj = hashlib.md5()
    BUFFER_SIZE = 1024

    if FileName is None or FileName == "":
        print("Invalid file name provided")
        return
    
    if not(os.path.isabs(FileName)):
        FileName = os.path.abspath(FileName)

    if not(os.path.exists(FileName)):
        print("There is no such a file")
        return
    
    if not(os.path.isfile(FileName)):
        print("Provided path is not a valid file")
        return
    
    fobj = None
    try:
        fobj = open(FileName, "rb")
        Buffer = fobj.read(BUFFER_SIZE)
        while len(Buffer) > 0:
            hobj.update(Buffer)
            Buffer = fobj.read(BUFFER_SIZE)
        
        CheckSum = hobj.hexdigest()

    except Exception as eobj:
        print(eobj)
    finally:
        if fobj is not None and not(fobj.closed):
            fobj. close()

    return CheckSum

