# Marvellous MAE Loss Demonstration

def Marvellous_MAE(y_true, y_pred):
    n = len(y_true)
    total_error = 0

    for i in range(n):
        error = abs(y_true[i] - y_pred[i])
        total_error += error

    mae = total_error / n
    return mae


# Sample Data
y_true = [10, 20, 30]
y_pred = [12, 18, 33]

loss = Marvellous_MAE(y_true, y_pred)
print("MAE Loss:", loss)