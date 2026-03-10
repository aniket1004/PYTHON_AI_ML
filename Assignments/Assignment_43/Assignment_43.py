import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def load_dataset(csv_path):
    dataframe = None
    try:

        dataframe = pd.read_csv(csv_path)
        if dataframe is not None:
            print(dataframe.head())

    except Exception as eobj:
        print(eobj)

    return dataframe

def label_encoder(le, series):
    result = None
    if series is not None:

        # le.fit(["paris", "paris", "tokyo", "amsterdam"])
        # list(le.classes_)
        # le.transform(["tokyo", "tokyo", "paris"])

        # fit_transform done both operation le.fit and le.transform
        result = le.transform(series)

    return result

def calculate_accuracy(y_test, y_pred):
    correct = 0
    total = 0
    for i in range(len(y_pred)):
        if y_test[i] == y_pred[i]:
            correct += 1
        total += 1

    return (correct/total)*100
    


def train_test_model(X, Y, K):
    
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.5)
    m = KNeighborsClassifier(n_neighbors=K)

    m = m.fit(x_train, y_train)

    y_pred = m.predict(x_test)

    accuracy = calculate_accuracy(list(y_test), list(y_pred))

    print(f"Accuracy of model with K {K} : {accuracy}")
    # Accuracy of model with K 3 : 80.0
    # Accuracy of model with K 5 : 66.66666666666666
    # Accuracy of model with K 7 : 73.33333333333333


def main():
    border = "-" * 80

    print(border)
    print("Step 1 : Load the dataset")
    print(border)

    csv_path = "PlayPredictor.csv"

    dataframe = load_dataset(csv_path)

    if dataframe is None:
        print("Failed to load dataset")
        return
    
    print(border)
    print("Step 2 : Weather and Temperature Encoding")
    print(border)

    le_whether = LabelEncoder()
    le_whether.fit(dataframe["Whether"])

    le_temperature = LabelEncoder()
    le_temperature.fit(dataframe["Temperature"])

    whether_encoding = label_encoder(le_whether, dataframe["Whether"])
    if whether_encoding is None:
        print("Failed to encode whether labels")

    dataframe["Whether_Encoding"] = whether_encoding

    temperature_encoding = label_encoder(le_temperature,dataframe["Temperature"])
    if temperature_encoding is None:
        print("Failed to encode temperature labels ")

    dataframe["Temperature_Encoding"] = temperature_encoding

    print(border)
    print("Step 3 : Train the model on whole dataset")
    print(border)

    model = KNeighborsClassifier(n_neighbors=3)

    features = ["Whether_Encoding", "Temperature_Encoding"]

    X = dataframe[features]
    Y = dataframe["Play"]

    model = model.fit(X, Y)

    print("Model training completed")

    print(border)
    print("Step 4 : Test the model on random values")
    print(border)

    X_test_dict = {
        "Whether" : ["Sunny", "Overcast", "Sunny", "Rainy"],
        "Temperature" : ["Hot", "Hot", "Mild", "Cool"]
    }
    dataframe_test = pd.DataFrame(X_test_dict)
    print(dataframe_test)

    dataframe_test["Whether_Encoding"] = label_encoder(le_whether,dataframe_test["Whether"])
    dataframe_test["Temperature_Encoding"] = label_encoder(le_temperature,dataframe_test["Temperature"])

    X_test = dataframe_test[features]
    
    print("Testing Result :")

    Y_pred = model.predict(X_test)

    X_test["Whether"] = le_whether.inverse_transform(X_test["Whether_Encoding"])
    X_test["Temperature"] = le_temperature.inverse_transform(X_test["Temperature_Encoding"])

    X_test["Play"] = Y_pred

    print(X_test)

    print(border)
    print("Step 5 : Calculate the accuracy by changing values of k")
    print(border)

    train_test_model(X, Y, 3)
    train_test_model(X, Y, 5)
    train_test_model(X, Y, 7)

if __name__ == "__main__":
    main()