from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    iris = load_iris()

    X = iris.data
    Y = iris.target

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy of model is : ", accuracy * 100)

if __name__ == "__main__":
    main()