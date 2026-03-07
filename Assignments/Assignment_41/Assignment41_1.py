import math
def Euclidean_Distance(X1, Y1, X2, Y2):
    Distance = 0.0

    Value = ((X2 - X1)**2) + ((Y2 - Y1)**2)

    Distance = math.sqrt(Value)

    return Distance

def main():

    border = "-" * 80

    Dataset = [
        {
            "Point" : "A",
            "X" : 1,
            "Y" : 2,
            "Label" : "Red"
        },
        {
            "Point" : "B",
            "X" : 2,
            "Y" : 3,
            "Label" : "Red"
        },
        {
            "Point" : "C",
            "X" : 3,
            "Y" : 1,
            "Label" : "Blue"
        },
        {
            "Point" : "D",
            "X" : 6,
            "Y" : 5,
            "Label" : "Blue"
        }
    ]

    print(border)
    print("Dataset loaded successfully")
    print(border)

    print("New Coordinate : ")
    print(border)
    print("Enter the X coordinate : ")
    X = int(input())

    print("Enter the Y coordinate : ")
    Y = int(input())

    
    
    for d in Dataset:
        Distance = Euclidean_Distance(d["X"], d["Y"], X, Y)
        d["Distance"] = Distance

    sorted_distance = sorted(Dataset, key= lambda d : d["Distance"])

    print(border)
    print("Sorted Distance : ")
    print(border)

    for d in sorted_distance:
        print(d)

    K = 3
    print(border)
    print(f"K = {K} for nearest neighbors :")
    print(border)

    sorted_distance_k = sorted_distance[:K]

    for d in sorted_distance_k:
        point = d["Point"]
        distance = d["Distance"]
        print("%s - Distance : %.2f" % (point, distance))

    votes = {}

    for d in sorted_distance_k:
        label = d["Label"]
        votes[label] = votes.get(label, 0) + 1
    
    print(border)
    print("Votes for K nearest neighbors :")
    print(border)

    for v in votes.keys():
        print(f"Label {v} : {votes[v]}")

    print(border)
    print("Predicted class label")
    print(border)
    
    y_pred = max(votes, key=votes.get)
    print(y_pred)
    
if __name__ == "__main__":
    main()