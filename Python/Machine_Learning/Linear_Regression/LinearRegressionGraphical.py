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

    n = len(X)  # 5

    # Y = mX + C

    # m = (summation (X - X_bar) * (Y - Y_bar)) / (summation (X - X_bar) ** 2)
    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x)*(Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)
    
    m = numerator / denominator

    print("Slope of line is  m : ", m) # 0.4

    # C = y_bar - (m * x_bar)
    C = mean_y - (m * mean_x)

    print("Y intercept of line is C : ", C)

    x = np.linspace(1, 6, n)
    print(x)
    y = C + m * x

    plt.plot(x, y, color = "g", label = "Regression Line")
    plt.scatter(X, Y, color = "r", label = "Scatter plot")

    plt.xlabel("X : Indepedent Variables")
    plt.ylabel("Y : Dependent Variables")

    plt.legend()
    plt.show()

    Y_p = []
    Y_p_summation = 0
    for i in range(n):
        value = (m * X[i]) + C
        Y_p.append(value)

    print(Y_p)

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()