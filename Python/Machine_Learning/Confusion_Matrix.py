from sklearn.metrics import confusion_matrix

def main():
    # 1 : Positive
    # 2 : Negative
    Actual = [1, 0, 1, 1, 1, 0, 1, 0, 0, 1]
    Predicted = [1, 0, 0, 1, 1, 1, 1, 1, 0, 1]

    print("Actual Data : ", Actual)
    print("Predicted Data : ", Predicted)

    confuse_mat = confusion_matrix(Actual, Predicted)
    print(confuse_mat)

if __name__ == "__main__":
    main()
