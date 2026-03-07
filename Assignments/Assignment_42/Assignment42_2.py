
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

    
    Y_Pred = []
    Y_Pred_Sum = 0

    for i in range(N):
        Yp = (Slope * X[i]) + C
        Y_Pred_Sum += Yp
        Y_Pred.append(Yp)

    print(border)
    print("Predicted Values of Y using regression equation")
    print(border)

    for i in range(N):
        print("Predicted Value for X = %d : %2f" % (X[i], Y_Pred[i]))

    # Mean_Square_Error = summation ((Y - Yp) ** 2) / N

    Numerator = 0
    for i in range(N):
        Numerator += ((Y[i] - Y_Pred[i]) ** 2)

    MSE = Numerator / N

    print(border)
    print("Mean_Square_Error = summation ((Y - Yp) ** 2) / N")
    print("Mean Squared Error (MSE) : ", MSE) # 0.72
    print(border)

    # R_Square = 1 - (summation ((Y - Ypred)**2)/ summation((Y - Ymean) ** 2))

    Numerator = 0
    Denominator = 0

    for i in range(N):
        Numerator += ((Y[i] - Y_Pred[i]) ** 2 )
        Denominator +=((Y[i] - Y_mean) ** 2)

    R2 = 1 - (Numerator /Denominator)

    print(border)
    print("R_Square = 1 - (summation ((Y - Ypred)**2)/ summation((Y - Ymean) ** 2))")
    print("R2 score is : ", R2) # 0.3076923076923078
    print(border)

if __name__ == "__main__":
    main()