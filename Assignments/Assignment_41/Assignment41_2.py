import math

border = "-" * 80

def Euclidean_Distance(X1, Y1, X2, Y2):
    Distance = 0.0

    Value = ((X2 - X1)**2) + ((Y2 - Y1)**2)

    Distance = math.sqrt(Value)

    return Distance

def Predict_Label(sorted_distance, k):
    global border
    sorted_distance_k = sorted_distance[:k]

    votes = {}
    print(sorted_distance_k)

    for d in sorted_distance_k:
        label = d["Label"]
        votes[label] = votes.get(label, 0) + 1

    print(border)
    print(f"Predicted class label with value K {k}")
    print(border)
    
    y_pred = max(votes, key=votes.get)
    print(y_pred)

def main():

    global border

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

    Predict_Label(sorted_distance, 1)
    Predict_Label(sorted_distance, 3)
    Predict_Label(sorted_distance, 5)

    
    
if __name__ == "__main__":
    main()