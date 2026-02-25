import seaborn as sns
import matplotlib.pyplot as plt

def main():

    sns.countplot(x= ["C", "C", "C++", "Java", "C++", "Python", "Javascript", "C++", "Golang", "C"])

    plt.show()

if __name__ == "__main__":
    main()