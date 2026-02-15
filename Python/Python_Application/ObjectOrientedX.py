class Arithmatic:

    def Addition(self, A, B):
        return A + B

    def Subtraction(self, A, B):
        return A - B

No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter first number:"))
No2 = int(input("Enter second number:"))

obj = Arithmatic()
Ans = obj.Addition(No1, No2)

print("Addition is:", Ans)

Ans = obj.Subtraction(No1, No2)

print("Subtraction is:", Ans)