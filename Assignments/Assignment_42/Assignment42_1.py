
border = "-" * 80

def Mean(Values):
    if Values == None or len(Values) == 0:
        return 0
    n = len(Values)
    Sum = 0

    for Val in Values:
        Sum += Val

    return Sum/n

def main():
    global border

    print(border)
    print("Simple Linear Regression")
    print(border)

    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    N = len(X)

    X_mean = Mean(X)
    Y_mean = Mean(Y)

    print("Mean of X (X_bar) : ",X_mean) # 3.0
    print("Mean of Y (Y_bar) : ",Y_mean) # 3.6

    Numerator = 0
    Denominator = 0

    #slope = summation (x - x_bar) * (y - y_bar) / summation ((x - x_bar) ** 2)
    for i in range(N):
        Numerator += ((X[i] - X_mean)* (Y[i] - Y_mean))
        Denominator += ((X[i] - X_mean) ** 2)
    
    Slope = Numerator/Denominator

    print("Slope (m) : ", Slope) # 0.4

    # y_intercept = y_bar - (m * x_bar)
    C = Y_mean - (Slope * X_mean)

    print("Intercept (c) : ", C) # 2.4

    X_pred = 6

    y_pred = (Slope * X_pred) + C

    print("Predicted Y for X = %d : %2f" % (X_pred, y_pred) )

if __name__ == "__main__":
    main()