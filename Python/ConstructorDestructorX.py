import gc

class Demo:
    def __init__(self):
        print("Inside Constructor")

    def __del__(self):
        print("Inside Destructor")

# Allocate object
obj1 = Demo()
obj2 = Demo()

# Use of object

# Deallocate object
del obj1
del obj2

gc.collect()

print("Enter of application")