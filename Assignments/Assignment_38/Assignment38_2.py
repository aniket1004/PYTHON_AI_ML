import pandas as pd
import os

border = "-" * 50
dataset_path = "student_performance_ml.csv"

def load_dataset_csv(path):
    dataframe = None
    if os.path.exists(path):
        dataframe = pd.read_csv(path)
    
    return dataframe

def main():
    global border
    global dataset_path

    ##########################################################
    # Load the dataset
    ##########################################################
    print(border)
    print("Load the dataset")  
    print(border)

    dataframe = load_dataset_csv(dataset_path)
    if dataframe is None:
        print("Please provide valid dataset file path.")
        return
    
    print("First 5 Records :")
    print(dataframe.head())

    print("First 5 Records :")
    print(dataframe.tail())

    print("Total number of rows : ", dataframe.shape[0])
    print("Total number of columns : ", dataframe.shape[1])

    print("List of column names :")
    print(list(dataframe.columns))

    print("Data type of columns are :")
    for column in list(dataframe.columns):
        print("Column name : " + column + " | Data Type : " + str(dataframe[column].dtype))

    print("Total number of student is : ", dataframe.shape[0])
    
    print("Total passed students is : ", (dataframe["FinalResult"] == 1).sum())
    print("Total failed students is : ", (dataframe["FinalResult"] == 0).sum())

if __name__ == "__main__":
    main()