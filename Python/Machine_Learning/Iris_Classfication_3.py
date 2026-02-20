from sklearn.datasets import load_iris

def main():
    print("Iris Classification Case Study")

    Dataset = load_iris()

    # Metadata of datasets
    print("Indepedent variables are : ")
    print(Dataset.feature_names)
    print("Length of independent variables is : ", len(Dataset.feature_names))
    
    print("Dependent variables are : ")
    print(Dataset.target_names)
    print("Length of dependent variables is : ", len(Dataset.target_names))

if __name__ == "__main__":
    main()
