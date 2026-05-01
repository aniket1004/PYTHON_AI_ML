# Marvellous MSE Loss Demonstration

def Marvellous_MSE(y_true, y_pred):
    n = len(y_true)
    total_error = 0

    for i in range(n):
        error = y_true[i] - y_pred[i]
        total_error += error ** 2   # Squared error

    mse = total_error / n
    return mse


# Sample Data
y_true = [10, 20, 30]
y_pred = [12, 18, 33]

loss = Marvellous_MSE(y_true, y_pred)
print("MSE Loss:", loss)