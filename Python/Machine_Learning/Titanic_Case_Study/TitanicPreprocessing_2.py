import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score



#------------------------------------------------------------------------------------------
# Function name :       DisplayInfo
# Description :              It displays the formated title.          
# Parameters :             Title (str)
# Return :                       None
# Date :                          14/03/2026
# Author :                      Aniket Chandrakant Dhole
#------------------------------------------------------------------------------------------

def DisplayInfo(Title):
    print("\n" + "=" * 80)
    print(Title)
    print("=" * 80)

#------------------------------------------------------------------------------------------
# Function name :       ShowData
# Description :              It shows basic information about dataset  
# Parameters :             Dataframe
#                                      Dataframe -> Pandas dataframe object
#                                      Message
#                                      Message -> Heading text to display
# Return :                       None
# Date :                          14/03/2026
# Author :                      Aniket Chandrakant Dhole
#------------------------------------------------------------------------------------------

def ShowData(Dataframe, Message):    
    DisplayInfo(Message)

    print("\nFirst 5 rows of dataset")
    print(Dataframe.head())

    print("\nShape of dataset")
    print(Dataframe.shape)

    print("\nColumn names :")
    print(Dataframe.columns.tolist())

    print("\nMissing values in each column :")
    print(Dataframe.isnull().sum())

#------------------------------------------------------------------------------------------
# Function name :       CleanTitanicData
# Description :              It does preprocessing
#                                      It removed unnecessary columns
#                                      It handles missing values
#                                      It converts text data to numeric format
#                                      It does encoding to categorical columns
# Parameters :             Dataframe
#                                      Dataframe -> Pandas dataframe
# Return :                       Dataframe -> Clean Pandas dataframe
# Date :                          14/03/2026
# Author :                      Aniket Chandrakant Dhole
#------------------------------------------------------------------------------------------

def CleanTitanicData(Dataframe):
    DisplayInfo("Step 2 : Original Data")
    print(Dataframe.head())

    # Remove unnecessary columns
    drop_columns = ["Passengerid", "zero", "Name", "Cabin"]
    existing_columns = [col for col in drop_columns if col in Dataframe.columns]

    print("\n Columns to be dropped : ")
    print(existing_columns)

    # drop the unwanted columns
    Dataframe = Dataframe.drop(columns = existing_columns)

    DisplayInfo("Step 2 : Data after columns removal")

    print(Dataframe.head())
    print(Dataframe.shape)

    # Handle age column
    if "Age" in Dataframe.columns:
        print("\nAge column before filling missing values :")
        print(Dataframe["Age"].head(10))

        # coerce -> Invalid value get converted to None
        Dataframe["Age"] = pd.to_numeric(Dataframe["Age"], errors="coerce")

        age_median = Dataframe["Age"].median()

        # Replace missing values with median
        Dataframe["Age"] = Dataframe["Age"].fillna(age_median)

        print("\nAge column after preprocessing :")
        print(Dataframe["Age"].head(10))

    # Handle fare column
    if "Fare" in Dataframe.columns:
        print("\nFare column before preprocessing")
        print(Dataframe["Fare"].head(10))

        Dataframe["Fare"] = pd.to_numeric(Dataframe["Fare"], errors="coerce")
        fare_median = Dataframe["Fare"].median()

        print("\nMedian of fare column is : ", fare_median)
        # Replace missing values with median
        Dataframe["Fare"] = Dataframe["Fare"].fillna(fare_median)

        print("\nFare column after preprocessing")
        print(Dataframe["Fare"].head(10))

    # Handle Embarked column
    if "Embarked" in Dataframe.columns:
        print("\nEmbarked column before preprocessing")
        print(Dataframe["Embarked"].head(10))

        # Convert the data into string
        Dataframe["Embarked"] = Dataframe["Embarked"].astype(str).str.strip()

        # Remove missing values
        Dataframe['Embarked'] = Dataframe["Embarked"].replace(['nan', 'None', ''], np.nan)

        # Get most frequent value
        embarked_mode = Dataframe["Embarked"].mode()[0]
        print("\nMode of embarked column : ", embarked_mode)

        Dataframe["Embarked"] = Dataframe["Embarked"].fillna(embarked_mode)

        print("\nEmbarked column after preprocessing")
        print(Dataframe["Embarked"].head(10))

    # Handle sex column
    if "Sex" in Dataframe.columns:
        print("\nSex column before preprocessing")
        print(Dataframe["Sex"].head(10))

        Dataframe["Sex"] = pd.to_numeric(Dataframe["Sex"], errors="coerce")

        print("\nSex column after preprocessing")
        print(Dataframe["Sex"].head(10))

    DisplayInfo("Data after preprocessing")
    print(Dataframe.head())

    print("\nMissing values after preprocessing")
    print(Dataframe.isnull().sum())

    return Dataframe

#------------------------------------------------------------------------------------------
# Function name :       MarvellousTitanicLogistic
# Description :              This is main pipeline controller
#                                      It loads the dataset, shows raw data
#                                      It preprocess the dataset & train the model           
# Parameters :             Data path of dataset file (str)
# Return :                       None
# Date :                          14/03/2026
# Author :                      Aniket Chandrakant Dhole
#------------------------------------------------------------------------------------------

def MarvellousTitanicLogistic(DataPath):
    DisplayInfo("Step 1 : Loading the dataset")
    df = pd.read_csv(DataPath)

    ShowData(df, "Initial dataset")

    df = CleanTitanicData(Dataframe=df)

#------------------------------------------------------------------------------------------
# Function name :       main
# Description :              Starting pont of the application           
# Parameters :             None
# Return :                       None
# Date :                          14/03/2026
# Author :                      Aniket Chandrakant Dhole
#------------------------------------------------------------------------------------------

def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()