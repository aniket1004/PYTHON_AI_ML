import pandas as pd

def main():
    Data = {
        "Name" : ["Sagar", "Amit", "Pooja"],
        "Age" : [23, 26, 25],
        "City" : ["Pune", "Mumbai", "Satara"]
    }

    dobj = pd.DataFrame(Data)

    print(dobj.loc[:, "Name"])

if __name__ == "__main__":
    main()