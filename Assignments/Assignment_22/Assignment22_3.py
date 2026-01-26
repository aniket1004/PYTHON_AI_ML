class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter the first number:", end=" ")
        self.Value1 = int(input())

        print("Enter the second number:", end=" ")
        self.Value2 = int(input())

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            return "Cannot divided by 0"
        return self.Value1 / self.Value2
    
aobj1 = Arithmetic()
aobj1.Accept()

result = aobj1.Addition()
print(f"Addition of numbers {aobj1.Value1} and {aobj1.Value2} is :", result)

result = aobj1.Subtraction()
print(f"Subtraction of numbers {aobj1.Value1} and {aobj1.Value2} is :", result)

result = aobj1.Multiplication()
print(f"Multiplication of numbers {aobj1.Value1} and {aobj1.Value2} is :", result)

result = aobj1.Division()
print(f"Division of numbers {aobj1.Value1} and {aobj1.Value2} is :", result)

aobj2 = Arithmetic()
aobj2.Accept()

result = aobj2.Addition()
print(f"Addition of numbers {aobj2.Value1} and {aobj2.Value2} is :", result)

result = aobj2.Subtraction()
print(f"Subtraction of numbers {aobj2.Value1} and {aobj2.Value2} is :", result)

result = aobj2.Multiplication()
print(f"Multiplication of numbers {aobj2.Value1} and {aobj2.Value2} is :", result)

result = aobj2.Division()
print(f"Division of numbers {aobj2.Value1} and {aobj2.Value2} is :", result)


