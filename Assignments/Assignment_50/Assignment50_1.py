import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

def main():
    dataset_path = "bank-full.csv"

    ############################################
    # Step 1 : Load the dataset
    ############################################
    df = pd.read_csv(dataset_path)

    print("First 5 records from dataset\n")
    print(df.head())
    print("Shape of dataset : ", df.shape)

    df.drop(columns=["contact", "default", "day", "month", "pdays", "poutcome"], inplace=True)
    df.dropna(inplace=True)

    df = df[ df["job"] != 'unknown' ]
    col_to_encode = ["job", "marital", "education", "housing", "loan", "y"]
    encoders = {}
    for col in col_to_encode:
        encoders[col] = LabelEncoder()
        df[col] = encoders[col].fit_transform(df[col])

    print("Shape of dataset after cleaning : ", df.shape)

    scalar = StandardScaler()

    X = df.drop(columns=["y"])
    Y = df["y"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train_scaled, Y_train)

    Y_pred = model.predict(X_test_scaled)

    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy of Logistic Regression is : ", accuracy * 100)
    print("Confusion matrix of Logistic Regression : \n", confusion_matrix(Y_test, Y_pred))
    print("Classification Report of Logistic Regression : \n", classification_report(Y_test, Y_pred))
    print("ROC -AUC score of Logistic Regression : ", roc_auc_score(Y_test, Y_pred))

    auc = roc_auc_score(Y_test, Y_pred)
    fpr, tpr, threshold = roc_curve(Y_test, Y_pred)

    plt.plot(fpr, tpr, label = f"Logistic Regression (AUC  = {auc:.2f})")
    plt.plot([0, 1], [0, 1], "k--", label="Random guessing (AUC = 0.5)")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC curve")
    plt.legend(loc="lower right")

    plt.show()

    print("-" * 80)

    model = KNeighborsClassifier()

    model.fit(X_train_scaled, Y_train)

    Y_pred = model.predict(X_test_scaled)

    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy of KNN is : ", accuracy * 100)
    print("Confusion matrix of KNN : \n", confusion_matrix(Y_test, Y_pred))
    print("Classification Report of KNN : \n", classification_report(Y_test, Y_pred))
    print("ROC -AUC score of KNN : ", roc_auc_score(Y_test, Y_pred))

    auc = roc_auc_score(Y_test, Y_pred)
    fpr, tpr, threshold = roc_curve(Y_test, Y_pred)

    plt.plot(fpr, tpr, label = f"KNN (AUC  = {auc:.2f})")
    plt.plot([0, 1], [0, 1], "k--", label="Random guessing (AUC = 0.5)")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC curve")
    plt.legend(loc="lower right")

    plt.show()

    model = RandomForestClassifier(n_estimators=501)
    model.fit(X_train_scaled, Y_train)

    Y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy of Random Forest Classifier is : ", accuracy * 100)
    print("Confusion matrix of Random Forest Classifier : \n", confusion_matrix(Y_test, Y_pred))
    print("Classification Report of Random Forest Classifier : \n", classification_report(Y_test, Y_pred))
    print("ROC -AUC score of Random Forest Classifier : ", roc_auc_score(Y_test, Y_pred))

    auc = roc_auc_score(Y_test, Y_pred)
    fpr, tpr, threshold = roc_curve(Y_test, Y_pred)

    plt.plot(fpr, tpr, label = f"Random forest (AUC  = {auc:.2f})")
    plt.plot([0, 1], [0, 1], "k--", label="Random guessing (AUC = 0.5)")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC curve")
    plt.legend(loc="lower right")

    plt.show()

if __name__ == "__main__":
    main()