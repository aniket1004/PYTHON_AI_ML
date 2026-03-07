import matplotlib.pyplot as plt
import numpy as np

border = "-" * 80

def main():
    global border

    # Experience = X
    # Salary = Y

    X = [1, 2, 3, 4, 5]
    Y = [20000, 25000, 30000, 35000, 40000]

    print (border)
    print("Dataset : ")
    print("Experience : ", X)
    print("Salary : ", Y)
    print(border)

    N = len(X)

    X_mean = np.mean(X)
    Y_mean = np.mean(Y)

    print("Mean of X : ", X_mean)
    print("Mean of Y : ", Y_mean)

    # Slope = (summation ((X - X_mean) * (Y - Y_mean)) / summation( (X - X_mean) ** 2))

    Numerator = 0
    Denominator = 0

    for i in range(N):
        Numerator += ((X[i] - X_mean) * (Y[i] - Y_mean))
        Denominator += ((X[i] - X_mean) ** 2)

    Slope = Numerator/ Denominator

    print("Slope of line (m) : ", Slope)

    # Intercept = Y_mean - (m * X_mean)

    C = Y_mean - (Slope * X_mean)

    print("Intercept (c) : ", C)

    X_test = 6
    Y_pred =  (Slope * X_test) + C
    print("Predicted Salary for 6 years Experience : Rs. ", Y_pred)

    plt.scatter(X, Y, color="orange", label = "Data points")

    X_array = np.array(X)
    plt.plot(X, Slope * X_array + C, color = "red", label = f"Regression line y = {Slope:.2f}X + {C:.2f}")

    plt.xlabel("Experience (in years)")
    plt.ylabel("Salary (in Ruppes)")

    plt.title("Scatter plot with regression line")

    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()