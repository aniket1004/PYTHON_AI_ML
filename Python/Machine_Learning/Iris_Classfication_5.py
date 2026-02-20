from sklearn.datasets import load_iris

def main():
    print("Iris Classification Case Study")

    Dataset = load_iris()

    Border = "-" * 40

    print(Border)

    for i in range(len(Dataset.target)):
        print("ID %d, Features %s, Label %s" % (i, Dataset.data[i], Dataset.target[i]))
    
    print(Border)

if __name__ == "__main__":
    main()
