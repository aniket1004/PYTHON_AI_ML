class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
        self.No1 = 10
        self.No2 = 20
    
    def fun(self):
        print("Inside fun method of parent", self.No1, self.No2)

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child contructor")
        self.A = 11
        self.B = 21

    def sun(self):
        print("Inside sun method of child", self.A, self.B, self.No1, self.No2)
        

cobj = Child()
print(cobj.No1) # 10
print(cobj.No2) # 20

print("-" * 25)

print(cobj.A)   # 11
print(cobj.B)   # 21

cobj.fun()
cobj.sun()