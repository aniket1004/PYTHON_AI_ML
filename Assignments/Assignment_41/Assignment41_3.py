import math

border = "-" * 80

def Euclidean_Distance(X1, Y1, X2, Y2):
    Ans = 0.0

    Value = ((X2 - X1) ** 2) + ((Y2 - Y1) ** 2)

    Ans = math.sqrt(Value)

    return Ans

def main():

    global border

    Dataset = [
        {
            "StudyHours" : 2,
            "Attendance" : 60,
            "Result" : "Fail"
        },
        {
            "StudyHours" : 5,
            "Attendance" : 80,
            "Result" : "Pass"
        },
        {
            "StudyHours" : 6,
            "Attendance" : 85,
            "Result" : "Pass"
        },
        {
            "StudyHours" : 1,
            "Attendance" : 50,
            "Result" : "Fail"
        }
    ]

    print(border)
    print("Dataset loaded successfully")
    print(border)

    print("New Input : ")
    print(border)
    print("Enter the Study Hours : ")
    X = int(input())

    print("Enter the Attendance : ")
    Y = int(input())

    
    
    for d in Dataset:
        Distance = Euclidean_Distance(d["StudyHours"], d["Attendance"], X, Y)
        d["Distance"] = Distance

    sorted_distance = sorted(Dataset, key = lambda d : d["Distance"]) 

    K = 3
    sorted_distance_k = sorted_distance[:K]
    
    votes = {}

    for d in sorted_distance_k:
        label = d["Result"]
        votes[label] = votes.get(label, 0) + 1

    y_pred = max(votes, key=votes.get)

    print("Predicted Result ", y_pred)

    
    
if __name__ == "__main__":
    main()