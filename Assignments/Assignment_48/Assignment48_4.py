import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def Euclidean_Distance(P1, P2):
    distance = 0
    result = ((P2["X"] - P1["X"]) ** 2) + ((P2["Y"] - P1["Y"]) ** 2)
    distance = np.sqrt(result)

    return distance
    
def main():
    dataset = {
        "P1" : {
            "X" : 25,
            "Y" : 20000
        },
        "P2" : {
            "X" : 30,
            "Y" : 40000
        }
    }

    distance = Euclidean_Distance(dataset["P1"], dataset["P2"])
    print("Distance between two points before scaling :", distance)

    X = []
    Y = []

    for point in dataset:
        X.append(dataset[point]["X"])
        Y.append(dataset[point]["Y"])

    X_mean = np.mean(X)
    Y_mean = np.mean(Y)

    Std_X = np.std(X)
    Std_Y = np.std(Y)

    print(X_mean, Std_X)
    print(Y_mean, Std_Y)

    for point in dataset:
        dataset[point]["X"] = (dataset[point]["X"] - X_mean)/ Std_X
        dataset[point]["Y"] = (dataset[point]["Y"] - Y_mean)/Std_Y

    print(dataset)
    distance = Euclidean_Distance(dataset["P1"], dataset["P2"])
    print("Distance between two points after scaling :", distance)

    # Before scaling value between X and Y values are so large.So value of X will be become less
    # important and result will be unbiased.abs
    # After scaling values both X and Y have equal importance and result will be based on both X and Y.

if __name__ == "__main__":
    main()