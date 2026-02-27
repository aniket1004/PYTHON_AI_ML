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

    print("Testing accuracy is ", accuracy*100)

    dict_list = [
        {
            "StudyHours" : 3.0,
            "Attendance" : 70,
            "PreviousScore" : 50,
            "AssignmentsCompleted" : 4,
            "SleepHours" : 6
        },
        {
            "StudyHours" : 6.0,
            "Attendance" : 80,
            "PreviousScore" : 60,
            "AssignmentsCompleted" : 8,
            "SleepHours" : 8
        },
        {
            "StudyHours" : 7.0,
            "Attendance" : 75,
            "PreviousScore" : 70,
            "AssignmentsCompleted" : 7,
            "SleepHours" : 7
        },
        {
            "StudyHours" : 2.0,
            "Attendance" : 75,
            "PreviousScore" : 45,
            "AssignmentsCompleted" : 8,
            "SleepHours" : 8
        },
        {
            "StudyHours" : 8.0,
            "Attendance" : 85,
            "PreviousScore" : 80,
            "AssignmentsCompleted" : 8,
            "SleepHours" : 8
        }
    ]
    new_dataframe = pd.DataFrame(dict_list)
    df_pred = model.predict(new_dataframe)
    print(df_pred)
    print("Study Hours\t|\tAttendance\t|\tPrevious Score\t|\tAssignments Completed\t|\tSleep Hours\t|\tFinalResult")
    index = 0
    for new_df in dict_list:
        print(new_df["StudyHours"], "\t\t|\t\t", new_df["Attendance"], "\t|\t", new_df["PreviousScore"],
        "\t\t|\t\t", new_df["AssignmentsCompleted"], "\t\t|\t\t", new_df["SleepHours"], "\t|\t", df_pred[index])
        #print(f"{new_df.get("StudyHours")}\t|\t{new_df.get("Attendance")}\t|\t{new_df.get("PreviousScore")}\t|\t{new_df.get("AssignmentsCompleted")}\t|\t{new_df.get("SleepHours")}\t|\t{df_pred[index]}")
        index += 1 
    
if __name__ == "__main__":
    main()