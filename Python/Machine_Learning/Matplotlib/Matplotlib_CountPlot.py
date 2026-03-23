import seaborn as sns
import matplotlib.pyplot as plt

def main():
    Data = ["A", "B", "A", "A", "B", "A", "C"]

    # Categorical Values
    sns.countplot(x= Data)

    plt.show()

if __name__ == "__main__":
    main()