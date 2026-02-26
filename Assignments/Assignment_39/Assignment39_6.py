import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    ConfusionMatrixDisplay, accuracy_score, classification_report, confusion_matrix
)

border = "-" * 50
dataset_path = "student_performance_ml.csv"

def load_dataset_csv(path):
    dataframe = None
    if os.path.exists(path):
        dataframe = pd.read_csv(path)
    
    return dataframe

def main():
    global border
    global dataset_path

    ##########################################################
    # Load the dataset
    ##########################################################
    print(border)
    print("Load the dataset")  
    print(border)

    dataframe = load_dataset_csv(dataset_path)
    if dataframe is None:
        print("Please provide valid dataset file path.")
        return
    
    print("First 5 Records :")
    print(dataframe.head())

    print("First 5 Records :")
    print(dataframe.tail())

    print("Total number of rows : ", dataframe.shape[0])
    print("Total number of columns : ", dataframe.shape[1])

    print("List of column names :")
    print(list(dataframe.columns))

    independent_variables = [
        "StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"
    ]
    X = dataframe[independent_variables]
    y = dataframe["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(criterion="gini", max_depth=None)

    model = model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    
    accuracy_testing = accuracy_score(Y_test, Y_pred)

    print("Testing Accuracy of model on Max Depth None is : ", accuracy_testing * 100, "%")

    model = DecisionTreeClassifier(criterion="gini", max_depth=1)

    model = model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    
    accuracy_testing = accuracy_score(Y_test, Y_pred)

    print("Testing Accuracy of model on Max Depth 1 is : ", accuracy_testing * 100, "%")

    model = DecisionTreeClassifier(criterion="gini", max_depth=3)

    model = model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    
    accuracy_testing = accuracy_score(Y_test, Y_pred)
    print("Testing Accuracy of model on Max Depth 3 is : ", accuracy_testing * 100, "%")
    
    # In above scenario max depth with values None, 1 and 3 accuracy always gives 100%.
    
if __name__ == "__main__":
    main()