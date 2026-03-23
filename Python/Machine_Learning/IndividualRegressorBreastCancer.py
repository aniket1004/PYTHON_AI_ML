import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

#-----------------------------------------------------------------------------
# Step 1 : Load the dataset
#-----------------------------------------------------------------------------
dataset_csv_name = "California_Housing.csv"
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
# Step 4 : Create base model
#-----------------------------------------------------------------------------
base_model = DecisionTreeRegressor(random_state=42)

#-----------------------------------------------------------------------------
# Step 5 : Train the bagging model
#-----------------------------------------------------------------------------
base_model.fit(X_train, Y_train)

#-----------------------------------------------------------------------------
# Step 6 : Test bagging model
#-----------------------------------------------------------------------------

Y_pred = base_model.predict(X_test)

#-----------------------------------------------------------------------------
# Step 7 : Evaluate the bagging model
#-----------------------------------------------------------------------------

print("Mean Squared Error : ", mean_squared_error(Y_test, Y_pred))
print("R2 Square : ", r2_score(Y_test, Y_pred))