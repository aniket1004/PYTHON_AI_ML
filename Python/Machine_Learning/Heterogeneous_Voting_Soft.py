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

    # Step 5 : Soft voting classification
    soft_model = VotingClassifier(
        estimators=[
            ('lr', model_lr),
            ('dt', model_dt),
            ('knn', model_knn)
        ],
        voting="soft"
    )

    soft_model.fit(X_train, Y_train)
    pred_soft = soft_model.predict(X_test)

    acc_soft = accuracy_score(Y_test, pred_soft)
    print("Accuracy of soft voting : ", acc_soft * 100)
    print("Confusion matrix of soft voting model : \n", confusion_matrix(Y_test, pred_soft))


if __name__ == "__main__":
    main()