import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
    accuracy_score, 
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
Border = "-" * 50
##########################################################################################################
# Step 1 : Load the dataset
##########################################################################################################
print(Border)
print("Step 1 : Load the dataset")
print(Border)

DataSet_Path = "iris.csv"
df = pd.read_csv(DataSet_Path)

print("Dataset gets loaded successfully")
print("Initial entries from dataset :")
print(df.head())

##########################################################################################################
# Step 2 : Data Analysis (EDA) 
##########################################################################################################
print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of dataset : ", df.shape)
print("Column names : ", list(df.columns))

print("Missing values (Per Column)")
print(df.isnull().sum())

print("Class Distribution (Species Count)")
print(df["variety"].value_counts())

print("Statistical Report of Dataset")
print(df.describe())
