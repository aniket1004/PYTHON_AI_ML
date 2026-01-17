from .Package.Marvellous import Add, Sub, PI

print("Inside Client", __name__)
print("Value of PI :", PI)

Result = 0

Result = Add(11, 10)
print("Addition is :", Result)

Result = Sub(43, 10)
print("Subtraction is :", Result)