class BankAccount:
    
    ROI = 10.5 # Rate of Interest

    def __init__(self, accountHolderName, accountBalance):
        self.Name = accountHolderName
        self.Amount = accountBalance

    def Display(self):
        print("Account holder name:", self.Name, "and current balance of account is:", self.Amount)

    def Deposit(self, amount):
        try:
            depositAmount = float(amount)
            self.Amount += depositAmount
        except ValueError as vobj:
            print("Amount should be a float value")

    def Withdraw(self, amount):
        try:
            withdrawAmount = float(amount)
            if withdrawAmount < 0.1:
                print("Withdraw amount should be greater than 0")
            else :
                if (self.Amount - withdrawAmount) > 0.5:
                    self.Amount -= withdrawAmount 
                else:
                    print("Withdrawal is not allowed, you have insufficient balance in account")
        except ValueError as vobj:
            print("Amount should be a float value")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest
    

obj1 = BankAccount("Aniket Chandrakant Dhole", 1000.0)

print("Initial Account Details Before Transaction")
obj1.Display()

obj1.Deposit(500)
obj1.Withdraw(100.0)

print("")
print("Account Details After Deposit and Withdraw Transactions")
obj1.Display()

print("")
interest = obj1.CalculateInterest()
print("Calculated rate of interest for your account is:", interest)




