import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error


def load_data(datapath):
    dataframe = None
    try:
        dataframe = pd.read_csv(datapath)
        print(dataframe.head())
    except Exception as eobj:
        print(eobj)
    
    return dataframe

def clean_prepare_data(df):
    if df is None :
        print("No data found")
        return
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)

    df.dropna(inplace=True)
    print("Cleaning and preparation of data completed")
    return df

def features_labels_divide(df, features, label):
    X = df[features]
    Y = df[label]

    return X, Y

def main():
    border = "-" * 50

    #-----------------------------------------------------------------
    # Step 1 : Load the data from csv
    #-----------------------------------------------------------------
    print(border)
    print("Step 1 : Load the data from csv")
    print(border)

    dataset_path = "Advertising.csv"

    df = load_data(dataset_path)
    if df is None:
        print("Unable to load the dataset")
        return

    #-----------------------------------------------------------------
    # Step 2 : Clean, prepare and manipulate data
    #-----------------------------------------------------------------
    print(border)
    print("Step 2 : Clean, prepare and manipulate data")
    print(border)

    df = clean_prepare_data(df)

    #-----------------------------------------------------------------
    # Step 3 : Train the data
    #-----------------------------------------------------------------
    print(border)
    print("Step 3 : Train the data")
    print(border)

    X = df.drop(columns=["sales"])
    Y = df["sales"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    model = LinearRegression()

    model.fit(X_train, Y_train)

    #-----------------------------------------------------------------
    # Step 4 : Test the data
    #-----------------------------------------------------------------
    print(border)
    print("Step 4 : Test the data")
    print(border)

    Y_pred = model.predict(X_test)

    MSE = mean_squared_error(Y_test, Y_pred)

    r2 = r2_score(Y_test, Y_pred)

    print("Mean squared error is :", MSE)
    print("R2 score : ", r2)
    
    #-----------------------------------------------------------------
    # Step 5 : Compare the actual and predicted values
    #-----------------------------------------------------------------
    print(border)
    print("Step 5 : Compare the actual and predicted values")
    print(border)

    dataframe = pd.DataFrame({
        "Actual Values" : Y_test.values,
        "Predicted Values" : Y_pred
    })

    print(dataframe)

    


if __name__ == "__main__":
    main()