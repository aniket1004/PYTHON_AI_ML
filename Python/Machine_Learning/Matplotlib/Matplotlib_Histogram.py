import seaborn as sns
import matplotlib.pyplot as plt

def main():
    Data = [10, 20, 30, 20, 20, 20, 30, 40]

    # Contigues Values
    sns.histplot(data= Data)

    plt.show()

if __name__ == "__main__":
    main()