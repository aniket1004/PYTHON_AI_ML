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
        "SleepHours" : [7, 6, 7, 6, 8],
        "Marks" : [50, 55, 60, 65, 70]
    }
    dataframe = pd.DataFrame(data)

    X = dataframe[["StudyHours", "SleepHours"]]
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

    
    columns_df = X.columns.values
    coef = list(model.coef_)
    for i in range(len(columns_df)):
        print(f"Coefficient of {columns_df[i]} is : {coef[i]}")
    print("Intercept is : ", model.intercept_)

if __name__ == "__main__":
    main()