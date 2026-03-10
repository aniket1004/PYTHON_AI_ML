from sklearn.datasets import load_iris

def main():
    print("Iris Classification Case Study")

    Dataset = load_iris()

    print(Dataset.data[0])
    print(Dataset.data[1])
    print(Dataset.data[2])
    print(Dataset.data[3])

    print(Dataset.target[0])
    print(Dataset.target[1])
    print(Dataset.target[2])
    print(Dataset.target[3])

    print(Dataset.target[50])
    print(Dataset.target[51])
    print(Dataset.target[52])
    print(Dataset.target[53])

    print(Dataset.target[100])
    print(Dataset.target[101])
    print(Dataset.target[102])
    print(Dataset.target[103])

if __name__ == "__main__":
    main()
