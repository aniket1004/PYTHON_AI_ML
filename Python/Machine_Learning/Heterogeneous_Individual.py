import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def main():

    # Step 1 : Load the dataset
    data = load_breast_cancer()
    
    X = data.data
    Y = data.target

    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)

    # Step 2 : Split the dataset
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Step 3 : Create base models
    model_lr = LogisticRegression(max_iter= 5000)
    model_dt = DecisionTreeClassifier(random_state= 42)
    model_knn = KNeighborsClassifier(n_neighbors= 5)

    # Step 4 : Train base models
    model_lr.fit(X_train, Y_train)
    model_dt.fit(X_train, Y_train)
    model_knn.fit(X_train, Y_train)

    # Step 5 : Calculate individual accuracy
    pred_lr = model_lr.predict(X_test)
    pred_dt = model_dt.predict(X_test)
    pred_knn = model_knn.predict(X_test)

    print("Accuracy of Logistic Regression : ", accuracy_score(Y_test, pred_lr) * 100)
    print("Accuracy of Decision Tree Classifier : ", accuracy_score(Y_test, pred_dt) * 100)
    print("Accuracy of K Nearest Neighbors : ", accuracy_score(Y_test, pred_knn) * 100)


if __name__ == "__main__":
    main()