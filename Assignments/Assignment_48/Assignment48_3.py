import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    dataset = [
        [25, 20000],
        [30, 40000],
        [35, 80000]
    ]
    
    scalar = StandardScaler()
    df_scaled = scalar.fit_transform(dataset)
    print(df_scaled)

if __name__ == "__main__":
    main()