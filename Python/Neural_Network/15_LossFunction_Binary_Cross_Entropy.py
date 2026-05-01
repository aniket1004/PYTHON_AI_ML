# Marvellous Binary Cross Entropy Demonstration
import math

def Marvellous_Binary_CrossEntropy(y_true, y_pred):
    total_loss = 0
    n = len(y_true)

    for i in range(n):
        y = y_true[i]
        p = y_pred[i]

        # Avoid log(0)
        p = max(min(p, 0.999), 0.001)

        loss = -(y * math.log(p) + (1 - y) * math.log(1 - p))
        total_loss += loss

    return total_loss / n


# Sample Data
y_true = [1, 0, 1]
y_pred = [0.9, 0.2, 0.8]

loss = Marvellous_Binary_CrossEntropy(y_true, y_pred)
print("Binary Cross Entropy Loss:", loss)