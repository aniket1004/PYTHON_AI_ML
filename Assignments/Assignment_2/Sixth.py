
def Addition(no1, no2):
    ans = None
    ans = no1 + no2
    return ans

def Subtraction(no1, no2):
    ans = None
    ans = no1 - no2
    return ans

def Multiplication(no1, no2):
    ans = None
    ans = no1 * no2
    return ans

def Division(no1, no2):
    ans = None
    if (no2 == 0):
        return "infinity"
    ans = no1 / no2
    return ans

print("Enter First Number:")
no1 = int(input())

print("Enter Second Number :")
no2 = int(input())

addition = Addition(no1, no2)
print("Addition of numbers is ", addition)

subtraction = Subtraction(no1, no2)
print("Subtraction of numbers is ", subtraction)

multiplication = Multiplication(no1, no2)
print("Multiplication of numbers is ", multiplication)

division = Division(no1, no2)
print("Division of numbers is ", division)

