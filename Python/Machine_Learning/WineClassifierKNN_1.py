import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

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

def main():
    border = "-" * 80

    print(border)
    print("Wine Classifier Using KNN")
    print(border)

    DataPath = "WinePredictor.csv"
    MarvellousClassifier(DataPath)

if __name__ == "__main__":
    main()