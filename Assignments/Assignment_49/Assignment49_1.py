import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier



def DisplayHeader(headerName):
    border = "=" * 80
    print(border)
    print(headerName)
    print(border)

def Main():
    dataset_path = "diabetes.csv"

    #=================================================================
    #  Step 1 : Exploratory Data Analysis (EDA)
    #=================================================================
    DisplayHeader("Step 1 : Exploratory Data Analysis (EDA)")

    dataframe = pd.read_csv(dataset_path)
    print("Dataset loaded successfully...")

    print("First few records of dataset : ")
    print(dataframe.head())

    print("Shape of dataset : ", dataframe.shape)

    print("Null value count : ")
    print(dataframe.isnull().value_counts())

    print("Statistics of dataset : ")
    print(dataframe.describe())

    X = dataframe.drop(columns=["Outcome"], axis=1)
    Y = dataframe["Outcome"]

    # plt.figure(figsize=(8,6))
    # plt.hist(Y, bins=2, color="skyblue", edgecolor="black")
    # plt.xlabel("Dependent Variable Outcome")
    # plt.ylabel("Count")
    # plt.show()

    # for key in X.columns.to_list():
    #     plt.boxplot(x = X[key], label=[key],vert=False)
    #     plt.xlabel(key)
    #     plt.title(f"Box plot to identify outliers in {key} records")
    #     #plt.savefig(f'boxplot_{key}.png', bbox_inches="tight")
        
    #     plt.show()

    # sns.pairplot(data=dataframe[["Insulin", "Outcome"]])
    # plt.show()

    print("Correlation between Independent and dependent variables : ")
    print(dataframe.corr())

    #=================================================================
    #  Step 2 : Data Preprocessing
    #=================================================================
    DisplayHeader("Step 2 : Data Preprocessing")
    print("Missing values from columns : ")
    print(dataframe.isnull().sum())

    dataframe.dropna(inplace=True)

    print("Shape of dataset after removing missing values : ", dataframe.shape)

    standard_scalar = StandardScaler()
    X_scaled = standard_scalar.fit_transform(X)

    #=================================================================
    #  Step 3 : Model building
    #=================================================================
    DisplayHeader("Step 3 : Model building")
    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

    # K  = 18 have 76.62337662337663 % accuracy
    # for k_value in range(1, 31): 
    #     knn_model = KNeighborsClassifier(n_neighbors=k_value)
    #     knn_model.fit(X_train, Y_train)
    #     Y_pred = knn_model.predict(X_test)

    #     print(f"Accuracy of k {k_value} : ", accuracy_score(Y_test, Y_pred) * 100) 

    
    logistic_model = LogisticRegression(max_iter=500)
    logistic_model.fit(X_train, Y_train)
    Y_pred = logistic_model.predict(X_test)
    print(f"Accuracy score of Logistics Regression model : ", accuracy_score(Y_test, Y_pred) * 100) 
    print(classification_report(Y_test, Y_pred))

    knn_model = KNeighborsClassifier(n_neighbors=19)
    knn_model.fit(X_train, Y_train)
    Y_pred = knn_model.predict(X_test)
    print(f"Accuracy of KNN model : ", accuracy_score(Y_test, Y_pred) * 100) 
    print(classification_report(Y_test, Y_pred))
    
    tree_model = DecisionTreeClassifier(random_state=42, max_depth=5)
    tree_model.fit(X_train, Y_train)
    Y_pred = tree_model.predict(X_test)
    print(f"Accuracy of Decision Tree model : ", accuracy_score(Y_test, Y_pred) * 100) 
    print(classification_report(Y_test, Y_pred))

if __name__ == "__main__":
    Main()