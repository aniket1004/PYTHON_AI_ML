import sklearn

# Rough = 1
# Smooth = 0

# Cricket = 2
# Tennis = 1
def main():
    print("Ball Classification Case Study")

    # Feature Encoding
    Features = [[35, 1], [47, 1], [90, 0], [48, 1],[90, 0],
        [35, 1], [92, 0], [35, 1], [35, 1], [35, 1], [96, 0], [43, 1],
        [110, 0], [35, 1], [95, 0]] 
    
    # Label Encoding
    Labels = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2]
    

if __name__ == "__main__":
    main()

# Dataset Size : 15