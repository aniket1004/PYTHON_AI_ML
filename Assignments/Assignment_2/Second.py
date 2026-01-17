# What is difference between (Explain using id())

a = 10
b = 10

print (id(a)) # 4342768752
print (id(b)) # 4342768752
# and

a = [10]
b = [10]

print (id(a)) # 4412117760
print (id(b)) # 4412275904