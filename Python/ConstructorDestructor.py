import gc

class Demo:
    def __init__(self):
        print("Inside Constructor")

    def __del__(self):
        print("Inside Destructor")

# Allocate object
obj = Demo()

# Use of object

# Deallocate object
del obj
gc.collect()

print("Enter of application")