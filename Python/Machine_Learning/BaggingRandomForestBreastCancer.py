import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#-----------------------------------------------------------------------------
# Step 1 : Load the dataset
#-----------------------------------------------------------------------------
dataset_csv_name = "Breast_Cancer.csv"
df = pd.read_csv(dataset_csv_name)
print("Shape of dataset : ", df.shape)
print("First 5 records of dataset : \n", df.head())

#-----------------------------------------------------------------------------
# Step 2 : Separate features and labels
#-----------------------------------------------------------------------------
X = df.drop(columns=["target"], axis=1)
Y = df["target"]

#-----------------------------------------------------------------------------
# Step 3 : Split dataset for training and testing
#-----------------------------------------------------------------------------
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#-----------------------------------------------------------------------------
# Step 4 : Create Random Forest  Model
#-----------------------------------------------------------------------------
rf_model = RandomForestClassifier(n_estimators=101, random_state=42)

#-----------------------------------------------------------------------------
# Step 5 : Train  model
#-----------------------------------------------------------------------------
rf_model.fit(X_train, Y_train)

#-----------------------------------------------------------------------------
# Step 6 : Test model
#-----------------------------------------------------------------------------

Y_pred = rf_model.predict(X_test)

#-----------------------------------------------------------------------------
# Step 7 : Evaluate  model
#-----------------------------------------------------------------------------

print("Bagging accuracy : ", accuracy_score(Y_test, Y_pred) * 100)

print("Confusion matrix : \n", confusion_matrix(Y_test, Y_pred))