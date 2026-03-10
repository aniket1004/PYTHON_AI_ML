import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def MarvellousPredictor():
    # Load the data
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    print("Values of indepedent variables : X - ", X)
    print("Values of depedent variables : Y - ",Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    print("Average/Mean of X is : ", mean_x)    # 3.0
    print("Average/Mean of Y is : ", mean_y)    # 3.6

    

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()