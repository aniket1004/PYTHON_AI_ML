import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    #---------------------------------------------------------------
    # Step 1 : Lod the dataset
    #---------------------------------------------------------------
    print("Step 1 : Load the dataset")
    df = pd.read_csv("Mall_Customers.csv")

    print("First few records : ")
    print(df.head())

    print("Shape of dataset : ")
    print(df.shape)

    print("Missing values : ")
    print(df.isnull().sum())

    #---------------------------------------------------------------
    # Step 2 : Select features (independent)
    #---------------------------------------------------------------
    print("Step 2 : Select features (independent)")

    X = df[ ["AnnualIncome", "SpendingScore"] ]
    print("Selected features : ")
    print(X.head())

    print("Shape of selected features : ")
    print(X.shape)

    #---------------------------------------------------------------
    # Step 3 : Scale the data
    #---------------------------------------------------------------
    print("Step 3 : Scale the data")

    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)

    print("Data after scaling : ")
    print(X_scaled[:5])

    #---------------------------------------------------------------
    # Step 4 : Use elbow method
    #---------------------------------------------------------------
    print("Step 4 : Use elbow method")

    WCSS = []

    for i in range(1, 11):
        model = KMeans(n_clusters=i, random_state=42, n_init=10)
        model.fit(X_scaled)

        WCSS.append(model.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, 11), WCSS, marker="o")
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow method")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()