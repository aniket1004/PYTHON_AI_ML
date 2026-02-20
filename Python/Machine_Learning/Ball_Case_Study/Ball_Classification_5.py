from sklearn import tree

# Rough = 1
# Smooth = 0

# Cricket = 2
# Tennis = 1
def main():
    print("Ball Classification Case Study")

    # Original Encoded Dataset
    # Independent Variables
    X = [[35, 1], [47, 1], [90, 0], [48, 1],[90, 0],
        [35, 1], [92, 0], [35, 1], [35, 1], [35, 1], [96, 0], [43, 1],
        [110, 0], [35, 1], [95, 0]] 
    
    # Dependent Variables
    Y = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2]

    # Independent variables for training
    XTrain = [[35, 1], [47, 1], [90, 0], [48, 1],[90, 0],
        [35, 1], [92, 0], [35, 1], [35, 1], [35, 1], [96, 0], [43, 1],
        [110, 0]] 
    # Dependent variables for training
    YTrain = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2]
    
    # Independent variables for testing
    XTest = [[35, 1], [95, 0]]
    # Dependent variables for testing
    YTest = [1, 2]
    
    model_obj = tree.DecisionTreeClassifier()
    
    trained_model = model_obj.fit(XTrain, YTrain)

    Result = trained_model.predict(XTest)    
    
    print("Model Predicts object as : ", Result) # [1 2]

if __name__ == "__main__":
    main()

# Dataset Size : 15