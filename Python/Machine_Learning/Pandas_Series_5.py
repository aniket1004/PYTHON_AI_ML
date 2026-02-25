import pandas as pd

def main():
    
    sobj = pd.Series([25000, 27000, 29000, 30000], index=["PPA", "LB", "PYTHON", "REACT"])

    print(sobj)

    print(sobj["PYTHON"])

if __name__ == "__main__":
    main()