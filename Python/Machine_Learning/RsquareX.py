from sklearn.metrics import r2_score

def main():
    Y_actual = [3, 4, 2, 4, 5]              # Y
    Y_predicted = [1.8, 1.2, 3.6, 1.0, 2.4] # Yp

    r2 = r2_score(Y_actual, Y_predicted)
    
    print("Actual values : Y ", Y_actual)
    print("Predicted values : Y ", Y_predicted)

    print("R Square value : ", r2) # -4.3076923076923075

if __name__ == "__main__":
    main()