import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    border = "-" * 80

    #----------------------------------------------------------------
    # Step 1 : Load the dataset from CSV file
    #----------------------------------------------------------------
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    dataframe = pd.read_csv(DataPath)

    print("Some entries from the dataset")
    print(dataframe.head())
    print(border)

    #----------------------------------------------------------------
    # Step 2 : Clean the dataset by removing empty cells
    #----------------------------------------------------------------
    print(border)
    print("Step 2 : Clean the dataset by removing empty cells")
    print(border)

    dataframe.dropna(inplace=True)
    print("Total records : ", dataframe.shape[0])
    print("Total columns : ", dataframe.shape[1])
    print(border)

    #----------------------------------------------------------------
    # Step 3 : Separate indepedent and dependent variables
    #----------------------------------------------------------------
    print(border)
    print("Step 3 : Separate indepedent and dependent variables")
    print(border)

    X = dataframe.drop(columns=["Class"])
    Y = dataframe["Class"]

    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)

    print(border)
    print("Input Columns : ", X.columns.to_list())
    print("Output Column : Class")

    #----------------------------------------------------------------
    # Step 4 : Split the dataset for training and testing
    #----------------------------------------------------------------
    print(border)
    print("Step 4 : Split the dataset for training and testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

    print(border)
    print("Information of training and testing data")
    print("X_train shape : ", X_train.shape)
    print("X_test shape : ", X_test.shape)
    print("Y_train shape : ", Y_train.shape)
    print("Y_test shape : ", Y_test.shape)
    print(border)

    
    #----------------------------------------------------------------
    # Step 5 : Feature scaling
    #----------------------------------------------------------------
    print(border)
    print("Step 5 : Feature scaling")
    print(border)

    scaler = StandardScaler()

    # Independent variable scaling
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("Feature scaling completed")


    #----------------------------------------------------------------
    # Step 6 : Explore the multiple values of K
    #----------------------------------------------------------------
    print(border)
    print("Step 6 : Explore the multiple values of K")
    print(border)
    # Hyperparameter tunning (K)

    accuracy_scores = []
    k_values = range(1, 21)

    for k in k_values:
        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train_scaled, Y_train)

        Y_pred = model.predict(X_test_scaled)

        accuracy = accuracy_score(Y_test, Y_pred)

        accuracy_scores.append(accuracy)

    print(border)
    print("Accuracy report of all k values from 1 to 20")
    for value in accuracy_scores:
        print(value)
    print(value)

    #----------------------------------------------------------------
    # Step 7 : Plot graph of K vs accuracy
    #----------------------------------------------------------------
    print(border)
    print("Step 7 : Plot graph of K vs Accuracy")
    print(border)

    plt.figure(figsize=(8,6))
    plt.plot(k_values, accuracy_scores, marker="o")
    plt.title("K values vs accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy of model")
    plt.grid()
    plt.xticks(list(k_values))
    
    plt.show()

    #----------------------------------------------------------------
    # Step 8 : Find best value of k
    #----------------------------------------------------------------
    print(border)
    print("Step 8 : Find best value of k")
    print(border)

    best_k = list(k_values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best value of K is : ", best_k)

    #----------------------------------------------------------------
    # Step 9 : Build the final model using value of k
    #----------------------------------------------------------------
    print(border)
    print("Step 9 : Build the final model using value of k")
    print(border)

    final_model = KNeighborsClassifier(n_neighbors=best_k)
    final_model.fit(X_train_scaled, Y_train)
    Y_pred = final_model.predict(X_test_scaled)

    #----------------------------------------------------------------
    # Step 10 : Calculate the final accuracy
    #----------------------------------------------------------------
    print(border)
    print("Step 10 : Calculate the final accuracy")
    print(border)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy of model is : ", accuracy * 100)

    #----------------------------------------------------------------
    # Step 11 : Display confusion matrix
    #----------------------------------------------------------------
    print(border)
    print("Step 11 : Display confusion matrix")
    print(border)

    cm = confusion_matrix(Y_test, Y_pred)
    print(cm)

    #----------------------------------------------------------------
    # Step 12 : Display classification report
    #----------------------------------------------------------------
    print(border)
    print("Step 12 : Display classification report")
    print(border)

    print(classification_report(Y_test, Y_pred))

def main():
    border = "-" * 80

    print(border)
    print("Wine Classifier Using KNN")
    print(border)

    DataPath = "WinePredictor.csv"
    MarvellousClassifier(DataPath)

if __name__ == "__main__":
    main()