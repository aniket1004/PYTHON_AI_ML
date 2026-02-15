No = 11 # Global

def Fun():
    No = 21 # Local
    print ("Value of no from Fun is", No)   # 21

print("Value of No is", No) # 11
Fun()