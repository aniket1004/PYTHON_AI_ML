import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import ( 
    accuracy_score, confusion_matrix, ConfusionMatrixDisplay
)

def dataset_loading(csv_path):
    dataframe = None

    dataframe = pd.read_csv(csv_path)

    if dataframe is not None:
        print("First 5 records : ")
        print(dataframe.head())

    return dataframe

def main():
    
    dataset_path = "student_performance_ml.csv"
    
    border = "-" * 50
    ###############################################################
    #   1. Dataset Loading
    ###############################################################
    print(border)
    print("1. Dataset Loading")
    print(border)

    dataframe = dataset_loading(dataset_path)

    if dataframe is None:
        print("Please check whether dataset is exist or not")
        return
    
    print("Dataset successfully loaded...")

    ###############################################################
    #   2. Dataset Analysis
    ###############################################################
    print(border)
    print("2. Dataset Analysis")
    print(border)

    correlation = dataframe.corr()
    print("Correlation between all contiguous features and labels with each other")
    print(correlation)

    print("")
    print("Description of dataset :")
    print(dataframe.describe())

    
    ###############################################################
    #   4. Train-Test Split of Dataset
    ###############################################################
    print(border)
    print("4. Train-Test Split of Dataset")
    print(border)

    # Train the model using only two features StudyHours and Attendance
    indepedent_variables = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]
    X = dataframe[indepedent_variables]
    Y = dataframe["FinalResult"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.8, random_state=42)

    print("Train-Test splitting completed...")

    ###############################################################
    #   5. Model Training
    ###############################################################
    print(border)
    print("5. Model Training")
    print(border)

    model = DecisionTreeClassifier(criterion="gini", max_depth=3)

    model = model.fit(X_train, Y_train)

    print("Model Training Completed")

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Testing accuracy by sklearn library is ", accuracy*100)

    correct = 0
    index = 0
    
    for i in list(Y_test):
        if i == Y_pred[index]:
            correct += 1
        index += 1

    accuracy = (correct/ len(Y_test))
    print("Testing accuracy by manually calculated is ", accuracy*100)

if __name__ == "__main__":
    main()