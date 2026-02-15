
class Demo:
    No = 10 # Class Variable

    def __init__ (self, A, B):
        self.Value1 = A     # Instance Variable
        self.Value2 = B     # Instance Variable

    def fun(self):
        print("Inside instance method fun", self.Value1, self.Value2)

    @classmethod
    def sun(cls):
        print("Inside class method sun",cls.No)

Demo.sun()
print("Class variable no:", Demo.No)

obj = Demo(11, 51)
obj.fun()
print("Instance variable:", obj.Value1, obj.Value2)