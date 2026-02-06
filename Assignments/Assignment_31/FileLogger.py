import time
import FileOperation

class FileLogger:

    def __init__(self, FileName):
        timestamp = time.ctime()
        self.FileName = FileOperation.GetFileNameWithoutExtension(FileName) + "_" + timestamp.replace(" ", "_").replace(":", "_") + "." + FileOperation.GetFileExtension(FileName)
        self.fobj = None
        try:
            self.fobj = open(self.FileName, "w")    
        except Exception as eobj:
            print(eobj)

    def WriteLine(self, Text, End = "\n"):
        if self.fobj is not None:
            self.fobj.write(Text)
            self.fobj.write(End)

    def WriteNextLine(self):
        if self.fobj is not None:
            self.fobj.write("\n")

    def WriteTab(self):
        if self.fobj is not None:
            self.fobj.write("\t")

    def WriteBorder(self, DashCount = 50, End = "\n"):
        if self.fobj is not None:
            self.fobj.write("-" * DashCount)
            self.fobj.write(End)

    def __del__(self):
        if self.fobj is not None and not(self.fobj.closed):
            self.fobj.close()
    

