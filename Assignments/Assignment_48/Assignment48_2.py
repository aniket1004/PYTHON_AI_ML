import numpy as np

def main():
    dataset = [6, 7, 8, 9, 10, 11, 12]

    mean = np.mean(dataset)

    sum = 0
    for num in dataset:
        sum += ((num - mean)**2)

    variance = sum / len(dataset)
    print("Variance is : ", variance)

    standard_deviation = np.sqrt(variance)
    print("Standard deviation is : ", standard_deviation)

if __name__ == "__main__":
    main()