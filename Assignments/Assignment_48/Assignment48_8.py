import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix


def main():
    Y_true = [1, 1, 1, 1, 0, 0, 0, 0]
    Y_pred= [1, 1, 0, 1, 0, 1, 0, 0]

    cm = confusion_matrix(Y_true, Y_pred)

    print("TP ", cm[0, 0])
    print("FN ", cm[0, 1])
    print("FP ", cm[1, 0])
    print("TN ", cm[1, 1])
    
    
if __name__ == "__main__":
    main()