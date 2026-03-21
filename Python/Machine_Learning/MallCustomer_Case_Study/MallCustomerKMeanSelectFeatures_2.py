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


if __name__ == "__main__":
    main()