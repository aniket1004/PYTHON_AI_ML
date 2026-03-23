import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Detecting Outliers
    sns.boxplot(x= [10, 20, 30, 110])

    plt.show()

if __name__ == "__main__":
    main()