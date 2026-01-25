# Dunder Method / Magic Method / Special Method

class Demo:
    def __init__(self, A):
        self.No = A

    def __add__(self,other):
        return self.No + other.No
    
    def __sub__(self,other):
        return self.No - other.No
    
    def __mul__(self,other):
        return self.No * other.No
    
    def __truediv__(self,other):
        return self.No / other.No
    
    # pow mod floordiv

obj1 = Demo(11)
obj2 = Demo(21)

print(obj1 + obj2)  # 32
print(obj1 - obj2)  # -10
print(obj1 * obj2)  # 231
print(obj1 / obj2)  # 32

