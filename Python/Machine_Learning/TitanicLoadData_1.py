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