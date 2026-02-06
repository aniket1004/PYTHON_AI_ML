import os

def IsDirectoryExist(DirectoryName):
    """
    This function is check whether given directory is exist or not.

    Args:
        DirectoryName (str) : The directory name.

    Returns:
        bool: True or False (Exist or Not)

    """
    
    if DirectoryName != "":
        if os.path.isdir(DirectoryName):
            return True
        
    return False

def GetFileExtension(FileName):
    Extension = None
    
    SplitList = FileName.split(".")
    if len(SplitList) > 1:
        Extension = SplitList[ len(SplitList)- 1 ]

    return Extension

def GetFileNameWithoutExtension(FileName):
    Name = ""
    SplitList = FileName.split(".")
    if len(SplitList) > 1:
        for i in range(len(SplitList)):
            if i < (len(SplitList) - 1):
                Name = Name + SplitList[i]
    else:
        Name = FileName
    
    return Name
