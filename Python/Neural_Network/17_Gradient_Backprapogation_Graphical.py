import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------------------------------------------------
# Marvellous ANN Example with Animated Graphics
# Demonstrates:
# 1. Forward propagation
# 2. Loss calculation
# 3. Backpropagation
# 4. Gradient descent weight update
# 5. Animated visual representation
# ---------------------------------------------------------

# Sigmoid activation function
def Marvellous_Sigmoid(value):
    return 1 / (1 + math.exp(-value))

# Derivative of sigmoid
def Marvellous_Sigmoid_Derivative(output):
    return output * (1 - output)

# ---------------------------------------------------------
# Input values
# ---------------------------------------------------------
x1 = 1.0
x2 = 2.0
target = 1.0

# ---------------------------------------------------------
# Initial weights and bias
# ---------------------------------------------------------
w1 = 0.5
w2 = -0.3
b = 0.1

# Learning rate
learning_rate = 0.1

# Number of training iterations
epochs = 20

# ---------------------------------------------------------
# Store training history for animation
# ---------------------------------------------------------
history = []

print("Initial Values")
print("w1 =", w1)
print("w2 =", w2)
print("b  =", b)
print("-" * 50)

# ---------------------------------------------------------
# Training loop
# ---------------------------------------------------------
for epoch in range(1, epochs + 1):

    # Step 1: Forward Propagation
    z = (x1 * w1) + (x2 * w2) + b
    output = Marvellous_Sigmoid(z)

    # Step 2: Loss Calculation
    loss = 0.5 * (target - output) ** 2

    # Step 3: Backpropagation
    dL_doutput = output - target
    doutput_dz = Marvellous_Sigmoid_Derivative(output)
    dL_dz = dL_doutput * doutput_dz

    dL_dw1 = dL_dz * x1
    dL_dw2 = dL_dz * x2
    dL_db = dL_dz

    # Store values before update for animation
    history.append({
        "epoch": epoch,
        "z": z,
        "output": output,
        "loss": loss,
        "w1": w1,
        "w2": w2,
        "b": b,
        "grad_w1": dL_dw1,
        "grad_w2": dL_dw2,
        "grad_b": dL_db
    })

    # Step 4: Gradient Descent
    w1 = w1 - (learning_rate * dL_dw1)
    w2 = w2 - (learning_rate * dL_dw2)
    b = b - (learning_rate * dL_db)

    # Print values
    print("Epoch:", epoch)
    print("Weighted Sum (z):", round(z, 4))
    print("Predicted Output :", round(output, 4))
    print("Target Output    :", target)
    print("Loss             :", round(loss, 6))
    print("Gradient dL/dw1  :", round(dL_dw1, 6))
    print("Gradient dL/dw2  :", round(dL_dw2, 6))
    print("Gradient dL/db   :", round(dL_db, 6))
    print("Updated w1       :", round(w1, 6))
    print("Updated w2       :", round(w2, 6))
    print("Updated b        :", round(b, 6))
    print("-" * 50)

print("Final Trained Values")
print("w1 =", round(w1, 6))
print("w2 =", round(w2, 6))
print("b  =", round(b, 6))

# ---------------------------------------------------------
# Matplotlib Animated Visualization
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 7))
plt.subplots_adjust(left=0.05, right=0.95, top=0.92, bottom=0.08)

# Node positions
x1_pos = (1, 5)
x2_pos = (1, 2)
bias_pos = (1, 8)
sum_pos = (5, 3.5)
out_pos = (9, 3.5)

# Draw neuron circles
def draw_circle(position, label, color="lightblue"):
    circle = plt.Circle(position, 0.5, color=color, ec="black", lw=2)
    ax.add_patch(circle)
    ax.text(position[0], position[1], label, ha='center', va='center', fontsize=12, weight='bold')

# Animation update function
def update(frame):
    ax.clear()
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 10)
    ax.axis("off")

    data = history[frame]

    # Title
    ax.text(5.5, 9.5, "Marvellous ANN Training Animation", ha='center',
            fontsize=18, weight='bold')

    # Draw nodes
    draw_circle(x1_pos, f"x1\n{x1}", "lightgreen")
    draw_circle(x2_pos, f"x2\n{x2}", "lightgreen")
    draw_circle(bias_pos, f"b\n{round(data['b'], 3)}", "khaki")
    draw_circle(sum_pos, f"z\n{round(data['z'], 3)}", "lightskyblue")
    draw_circle(out_pos, f"ŷ\n{round(data['output'], 3)}", "salmon")

    # Draw arrows
    ax.annotate("", xy=sum_pos, xytext=x1_pos,
                arrowprops=dict(arrowstyle="->", lw=2))
    ax.annotate("", xy=sum_pos, xytext=x2_pos,
                arrowprops=dict(arrowstyle="->", lw=2))
    ax.annotate("", xy=sum_pos, xytext=bias_pos,
                arrowprops=dict(arrowstyle="->", lw=2))
    ax.annotate("", xy=out_pos, xytext=sum_pos,
                arrowprops=dict(arrowstyle="->", lw=2))

    # Show weights on arrows
    ax.text(2.7, 4.7, f"w1 = {round(data['w1'], 3)}", fontsize=11, weight='bold')
    ax.text(2.7, 2.4, f"w2 = {round(data['w2'], 3)}", fontsize=11, weight='bold')
    ax.text(2.6, 6.8, f"bias", fontsize=11, weight='bold')

    # Formula display
    ax.text(5.5, 1.2,
            f"z = (x1*w1) + (x2*w2) + b = ({x1}*{round(data['w1'],3)}) + ({x2}*{round(data['w2'],3)}) + {round(data['b'],3)}",
            ha='center', fontsize=11)

    ax.text(5.5, 0.6,
            f"Loss = 0.5 * (target - output)^2 = 0.5 * ({target} - {round(data['output'],3)})^2 = {round(data['loss'],6)}",
            ha='center', fontsize=11, color='red')

    # Epoch and gradients
    ax.text(8.8, 8.0, f"Epoch : {data['epoch']}", fontsize=13, weight='bold')
    ax.text(8.0, 7.2, f"dL/dw1 = {round(data['grad_w1'], 6)}", fontsize=11)
    ax.text(8.0, 6.6, f"dL/dw2 = {round(data['grad_w2'], 6)}", fontsize=11)
    ax.text(8.0, 6.0, f"dL/db  = {round(data['grad_b'], 6)}", fontsize=11)

    # Target display
    ax.text(9, 2.0, f"Target = {target}", fontsize=12, weight='bold', color='blue')

    # Loss status
    ax.text(8.0, 5.0, f"Current Loss = {round(data['loss'], 6)}",
            fontsize=12, weight='bold', color='darkred')

# Create animation
ani = FuncAnimation(fig, update, frames=len(history), interval=1000, repeat=False)

plt.show()