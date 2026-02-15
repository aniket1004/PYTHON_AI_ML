No = 11 # Global

def Fun():
    global No
    print ("Value of no from Fun is", No)   # 11
    No = No + 1
    print ("Value of no from Fun is", No) # 12

print("Value of No is", No) # 11
Fun()
print("Value of No is", No) # 12