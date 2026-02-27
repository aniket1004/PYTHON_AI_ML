import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import ( 
    accuracy_score, confusion_matrix, ConfusionMatrixDisplay
)
border = "-" * 50
def dataset_loading(csv_path):
    dataframe = None

    dataframe = pd.read_csv(csv_path)

    if dataframe is not None:
        print("First 5 records : ")
        print(dataframe.head())

    return dataframe

def train_test_model(X, Y, random_state):
    global border
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

    print(f"Testing accuracy with random state {random_state} is ", accuracy*100)


def main():
    global border
    dataset_path = "student_performance_ml.csv"
    
    
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

    indepedent_variables = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]
    X = dataframe[indepedent_variables]
    Y = dataframe["FinalResult"]

    train_test_model(X, Y, 0)
    train_test_model(X, Y, 10)
    train_test_model(X, Y, 42)
    
if __name__ == "__main__":
    main()