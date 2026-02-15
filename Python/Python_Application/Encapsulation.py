class Arithmatic:
    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B
        print("Objects get created successfully")
        
    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Subtraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans
    
obj1 = Arithmatic(11, 10)
obj2 = Arithmatic(21, 20)

Ret = obj1.Addition()
print(Ret) # 21

Ret = obj2.Subtraction()
print(Ret) # 1


    
