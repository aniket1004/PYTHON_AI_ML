import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    dobj = pd.DataFrame(
        {
            "A" : [1, 2, 3],
            "B" : [4, 5, 6],
            "C" : [7, 8, 9]
        }
    )
    print(dobj)
    
    # Feature correlation 
    sns.heatmap(dobj.corr(), annot=True)

    plt.show()

if __name__ == "__main__":
    main()