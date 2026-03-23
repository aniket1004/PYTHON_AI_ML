import pandas as pd
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target

df.to_csv("California_Housing.csv", index=False)

print("California Housing csv get created successfully")