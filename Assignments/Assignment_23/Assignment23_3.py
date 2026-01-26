
class Numbers:

    def __init__(self):
        self.Value = 0
        print("-" * 50)
        print("Enter the number:", end=" ")
        try:
            self.Value = int(input())
        except ValueError as vobj:
            print("Input value should be numeric")


    def ChkPrime(self):
        isPrime = False
        for i in range(2, self.Value + 1):
            if i == self.Value:
                isPrime = True
                break
            else:
                if self.Value % i == 0:
                    isPrime = False
                    break

        return isPrime

    def Factors(self):
        fact = list()
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                fact.append(i)
        return fact
    
    def SumFactors(self):
        Sum = 0
        factors = self.Factors()
        for i in range(len(factors)):
            Sum += factors[i]
        return Sum
    
    def ChkPerfect(self):
        isPerfect = False
        Sum = self.SumFactors()
        Sum = Sum - self.Value
        if Sum == self.Value:
            isPerfect = True
        
        return isPerfect
    
obj1 = Numbers()
if obj1.ChkPrime():
    print(f"Given number {obj1.Value} is prime")
else:
    print(f"Given number {obj1.Value} is not prime")

factors = obj1.Factors()
print(f"Factors of given number {obj1.Value} is:", end=" ")
for i in factors:
    print(i, end="  ")

print("")

Sum = obj1.SumFactors()
print(f"Sum of factors of given number {obj1.Value} is:", Sum)

if obj1.ChkPerfect():
    print(f"Given number {obj1.Value} is perfect number")
else:
    print(f"Given number {obj1.Value} is not perfect number")


obj2 = Numbers()
if obj2.ChkPrime():
    print(f"Given number {obj2.Value} is prime")
else:
    print(f"Given number {obj2.Value} is not prime")

factors = obj2.Factors()
print(f"Factors of given number {obj2.Value} is:", end=" ")
for i in factors:
    print(i, end="  ")

print("")

Sum = obj2.SumFactors()
print(f"Sum of factors of given number {obj2.Value} is:", Sum)

if obj2.ChkPerfect():
    print(f"Given number {obj2.Value} is perfect number")
else:
    print(f"Given number {obj2.Value} is not perfect number")
