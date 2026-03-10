#   [A, B, C, D]
# X [1, 2, 3, 5]
# Y [2, 3, 1, 6]
#   [R, R, B, B]

# Predict (3, 3) -> ?
import numpy as np
import math

def EucDistance(P1, P2):
    Ans = math.sqrt((P1["X"] - P2["X"]) ** 2 + (P1["Y"] - P2["Y"]) ** 2)
    return Ans

def MarvellousKNeighborsClassifier():
    border = "-" * 50
    data = [
        {"point" : "A", "X" : 1, "Y" : 2, "label" : "R"},
        {"point" : "B", "X" : 2, "Y" : 3, "label" : "R"},
        {"point" : "C", "X" : 3, "Y" : 1, "label" : "B"},
        {"point" : "D", "X" : 5, "Y" : 6, "label" : "B"},
    ]

    print(border)
    print("Marvellous User Defined KNN")
    print(border)

    print(border)
    print("Training Dataset")
    print(border)

    for d in data:
        print(d)
    
    print(border)

    new_point = {"X" : 3, "Y" : 3}

    # Calculate All Distances
    for d in data:
        d["distance"] = EucDistance(new_point, d)

    print(border)
    print("Calculated distances are :")
    print(border)

    for i in data:
        print(i)

    sorted_data = sorted(data, key= lambda item : item["distance"])
    
    print(border)
    print("Sorted data is :")
    print(border)

    for d in sorted_data:
        print(d)

    k = 3
    nearest = sorted_data[:k]
    print(border)
    print("Nearest 3 elements are :")
    print(border)

    for d in nearest:
        print(d)

    # Voting 
    votes = {}

    for neighbor in nearest:
        label = neighbor["label"]
        votes[label] = votes.get(label, 0) + 1

    print(border)
    print("Voting result is :")
    print(border)

    for d in votes.keys():
        print("Name is ", d, " Number of votes : ", votes[d])


    print(border)

def main():
    MarvellousKNeighborsClassifier()

if __name__ == "__main__":
    main()