
class Demo:
    No = 10 # Class Variable

    def __init__ (self, A, B):
        self.Value1 = A     # Instance Variable
        self.Value2 = B     # Instance Variable

print("Class variable:", Demo.No)
obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

print("Instance variable of obj1:", obj1.Value1, obj1.Value2)
print("Instance variable of obj2:", obj2.Value1, obj2.Value2)