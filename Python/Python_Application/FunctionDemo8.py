# Accept : Multiple Parameters
# Return : Multiple Values
def Marvellous1(Value1, Value2):
    print("Inside Marvellous1 :", Value1, Value2)
    return 11, 21, 51

def main():
    Result1 = None
    Result2 = None
    Result3 = None
    
    Result1, Result2, Result3 = Marvellous1("Python", 21)
    print("Return values are:", Result1, Result2, Result3)

if __name__ == "__main__":
    main()