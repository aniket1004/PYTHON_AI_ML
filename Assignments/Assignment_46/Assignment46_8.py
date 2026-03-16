import pandas as pd
from sklearn.linear_model import LinearRegression

def main():
    border = "-" * 80
    #------------------------------------------------------------
    # Step 1 : Set dataset
    #------------------------------------------------------------
    print(border)
    print("Step 1 : Dataset loading")
    print(border)

    data = {
        "StudyHours" : [1, 2, 3, 4, 5],
        "Marks" : [50, 55, 60, 65, 70]
    }
    dataframe = pd.DataFrame(data)

    X = dataframe[["StudyHours"]]
    Y = dataframe["Marks"]
    print("Independent Variable X : \n", X)
    print("Dependent Variable Y : \n", Y)
    #------------------------------------------------------------
    # Step 2 : Train the model
    #------------------------------------------------------------
    print(border)
    print("Step 2 : Train the model")
    print(border)

    model = LinearRegression()

    model.fit(X, Y)


    print("Coefficient is : ", model.coef_)
    print("Intercept is : ", model.intercept_)

    #------------------------------------------------------------
    # Step 3 : Predict the value
    #------------------------------------------------------------
    print(border)
    print("Step 3 : Predict the value")
    print(border)

    X_test_df = {
        "StudyHours" : [6]
    }
    X_test = pd.DataFrame(X_test_df)
    print(X_test)
    Y_pred = model.predict(X_test)
    print("Predicted marks for 6 study hours : ", Y_pred[0])

if __name__ == "__main__":
    main()