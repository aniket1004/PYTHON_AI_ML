import time

class FileLogger:

    def __init__(self, FileName):
        timestamp = time.ctime()
        self.FileName = FileName
        self.FileName = self.GetFileNameWithoutExtension() + "_" + timestamp.replace(" ", "_").replace(":", "_") + "." + self.GetFileExtension()
        self.fobj = None
        try:
            self.fobj = open(self.FileName, "w")    
        except Exception as eobj:
            print(eobj)

    def GetFileExtension(self):
        Extension = None
        
        SplitList = self.FileName.split(".")
        if len(SplitList) > 1:
            Extension = SplitList[ len(SplitList)- 1 ]

        return Extension

    def GetFileNameWithoutExtension(self):
        Name = ""
        SplitList = self.FileName.split(".")
        if len(SplitList) > 1:
            for i in range(len(SplitList)):
                if i < (len(SplitList) - 1):
                    Name = Name + SplitList[i]
        else:
            Name = self.FileName
        
        return Name

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
    

