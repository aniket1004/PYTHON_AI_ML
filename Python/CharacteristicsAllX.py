
class Demo:
    No = 10 # Class Variable

    def __init__ (self, A, B):
        self.Value1 = A     # Instance Variable
        self.Value2 = B     # Instance Variable

print("Class variable:", Demo.No)
obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

#print(obj1.No) # Allowed

print("Instance variable of obj1:", obj1.Value1, obj1.Value2)   # 11 21
print("Instance variable of obj2:", obj2.Value1, obj2.Value2)   # 51 101

obj1.Value1 = 15

Demo.No = 0

print("Instance variable of obj1:", obj1.Value1, obj1.Value2)   # 15 21
print("Instance variable of obj2:", obj2.Value1, obj2.Value2)   # 51 101

print(Demo.No)  # 0
print(obj1.No)  # 0
print(obj2.No)  # 0