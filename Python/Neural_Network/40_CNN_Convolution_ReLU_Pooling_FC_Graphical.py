import numpy as np
import matplotlib.pyplot as plt
import time

# ------------------------------------------------------------
# Function to display matrix
# ------------------------------------------------------------
def Marvellous_Display(matrix, title):
    plt.figure(figsize=(4, 4))
    plt.imshow(matrix, cmap='gray', interpolation='nearest')
    plt.title(title)
    plt.colorbar()

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            plt.text(j, i, f"{matrix[i][j]:.1f}",
                     ha='center', va='center',
                     color='red', fontsize=12)

    plt.show()

# ------------------------------------------------------------
# Function to display highlighted region animation
# ------------------------------------------------------------
def Marvellous_ShowConvolutionStep(image, kernel, start_row, start_col, current_output=None, step_title=""):
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))

    # ---------------- Image with highlighted region ----------------
    axes[0].imshow(image, cmap='gray', interpolation='nearest')
    axes[0].set_title("Input Image")
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            color = 'red'
            axes[0].text(j, i, f"{int(image[i][j])}", ha='center', va='center', color=color, fontsize=12)

    # Draw rectangle for active region
    rect_x = start_col - 0.5
    rect_y = start_row - 0.5
    rectangle = plt.Rectangle((rect_x, rect_y), 3, 3, fill=False, edgecolor='yellow', linewidth=3)
    axes[0].add_patch(rectangle)

    # ---------------- Kernel ----------------
    axes[1].imshow(kernel, cmap='gray', interpolation='nearest')
    axes[1].set_title("Kernel")
    for i in range(kernel.shape[0]):
        for j in range(kernel.shape[1]):
            axes[1].text(j, i, f"{int(kernel[i][j])}", ha='center', va='center', color='red', fontsize=12)

    # ---------------- Output Map ----------------
    if current_output is None:
        current_output = np.zeros((3, 3))

    axes[2].imshow(current_output, cmap='gray', interpolation='nearest')
    axes[2].set_title(step_title)
    for i in range(current_output.shape[0]):
        for j in range(current_output.shape[1]):
            axes[2].text(j, i, f"{current_output[i][j]:.1f}", ha='center', va='center', color='red', fontsize=12)

    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------
# Function for Convolution with animation
# ------------------------------------------------------------
def Marvellous_Convolution_Animated(image, kernel, delay=1.5):

    rows, cols = image.shape
    krows, kcols = kernel.shape

    output_rows = rows - krows + 1
    output_cols = cols - kcols + 1

    output = np.zeros((output_rows, output_cols))

    print("\n" + "-" * 60)
    print("STEP 1 : CONVOLUTION LAYER")
    print("-" * 60)

    for i in range(output_rows):
        for j in range(output_cols):
            region = image[i:i+krows, j:j+kcols]
            multiplication = region * kernel
            result = np.sum(multiplication)
            output[i][j] = result

            print(f"\nConvolution Region Position -> Row:{i}, Col:{j}")
            print("\nSelected Region:")
            print(region)
            print("\nKernel:")
            print(kernel)
            print("\nRegion * Kernel:")
            print(multiplication)
            print("\nSum =", result)

            Marvellous_ShowConvolutionStep(
                image,
                kernel,
                i,
                j,
                output,
                step_title=f"Feature Map Building (Row {i}, Col {j})"
            )
            time.sleep(delay)

    print("\nFinal Convolution Output:")
    print(output)

    return output

# ------------------------------------------------------------
# ReLU Function
# ------------------------------------------------------------
def Marvellous_ReLU(data):

    print("\n" + "-" * 60)
    print("STEP 2 : RELU ACTIVATION")
    print("-" * 60)

    output = np.maximum(0, data)

    print("\nInput to ReLU:")
    print(data)

    print("\nOutput after ReLU:")
    print(output)

    return output

# ------------------------------------------------------------
# Pooling animation display
# ------------------------------------------------------------
def Marvellous_ShowPoolingStep(feature_map, start_row, start_col, current_output=None, step_title=""):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].imshow(feature_map, cmap='gray', interpolation='nearest')
    axes[0].set_title("ReLU Output")

    for i in range(feature_map.shape[0]):
        for j in range(feature_map.shape[1]):
            axes[0].text(j, i, f"{feature_map[i][j]:.1f}", ha='center', va='center', color='red', fontsize=12)

    rect_x = start_col - 0.5
    rect_y = start_row - 0.5
    rectangle = plt.Rectangle((rect_x, rect_y), 2, 2, fill=False, edgecolor='yellow', linewidth=3)
    axes[0].add_patch(rectangle)

    if current_output is None:
        current_output = np.zeros((1, 1))

    axes[1].imshow(current_output, cmap='gray', interpolation='nearest')
    axes[1].set_title(step_title)

    for i in range(current_output.shape[0]):
        for j in range(current_output.shape[1]):
            axes[1].text(j, i, f"{current_output[i][j]:.1f}", ha='center', va='center', color='red', fontsize=12)

    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------
# Max Pooling with animation
# ------------------------------------------------------------
def Marvellous_Pooling_Animated(data, delay=1.5):

    rows, cols = data.shape
    output_rows = rows // 2
    output_cols = cols // 2

    output = np.zeros((output_rows, output_cols))

    print("\n" + "-" * 60)
    print("STEP 3 : MAX POOLING")
    print("-" * 60)

    r = 0
    for i in range(0, rows, 2):
        c = 0
        for j in range(0, cols, 2):

            block = data[i:i+2, j:j+2]

            if block.shape != (2, 2):
                continue

            max_value = np.max(block)
            output[r][c] = max_value

            print(f"\nPooling Block Position -> Row:{r}, Col:{c}")
            print("\nSelected Block:")
            print(block)
            print("\nMaximum Value =", max_value)

            Marvellous_ShowPoolingStep(
                data,
                i,
                j,
                output,
                step_title=f"Pooling Output (Row {r}, Col {c})"
            )
            time.sleep(delay)

            c += 1
        r += 1

    print("\nFinal Pooling Output:")
    print(output)

    return output

# ------------------------------------------------------------
# Flatten Layer
# ------------------------------------------------------------
def Marvellous_Flatten(data):

    print("\n" + "-" * 60)
    print("STEP 4 : FLATTEN LAYER")
    print("-" * 60)

    flat = data.flatten()

    print("\nInput to Flatten:")
    print(data)

    print("\nFlattened Output:")
    print(flat)

    return flat

# ------------------------------------------------------------
# Fully Connected Layer
# ------------------------------------------------------------
def Marvellous_FC(flat_data):

    print("\n" + "-" * 60)
    print("STEP 5 : FULLY CONNECTED LAYER")
    print("-" * 60)

    # Match weight count to flattened size
    weights = np.ones(len(flat_data))
    bias = 0.0

    print("\nFlatten Input:")
    print(flat_data)

    print("\nWeights:")
    print(weights)

    multiplication = flat_data * weights
    result = np.sum(multiplication) + bias

    print("\nInput * Weights:")
    print(multiplication)

    print("\nSum =", np.sum(multiplication))
    print("Bias =", bias)
    print("Final Score =", result)

    return result

# ------------------------------------------------------------
# Function to show final CNN pipeline summary
# ------------------------------------------------------------
def Marvellous_ShowPipeline(image, conv, relu, pool):
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))

    matrices = [image, conv, relu, pool]
    titles = ["Input Image", "Convolution Output", "ReLU Output", "Pooling Output"]

    for idx in range(4):
        axes[idx].imshow(matrices[idx], cmap='gray', interpolation='nearest')
        axes[idx].set_title(titles[idx])

        for i in range(matrices[idx].shape[0]):
            for j in range(matrices[idx].shape[1]):
                axes[idx].text(j, i, f"{matrices[idx][i][j]:.1f}",
                               ha='center', va='center',
                               color='red', fontsize=10)

    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------
# Main Function
# ------------------------------------------------------------
def Marvellous_CNN_Animated():

    print("Choose Input Image")
    print("1 : Vertical Line")
    print("2 : Horizontal Line")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        image = np.array([
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0]
        ], dtype=float)
        actual = "Vertical Line"
    else:
        image = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ], dtype=float)
        actual = "Horizontal Line"

    print("\n" + "-" * 60)
    print("INPUT IMAGE")
    print("-" * 60)
    print("\nActual Input =", actual)
    print(image)
    Marvellous_Display(image, "Input Image")

    kernel = np.array([
        [-1,  1, -1],
        [-1,  1, -1],
        [-1,  1, -1]
    ], dtype=float)

    print("\n" + "-" * 60)
    print("KERNEL")
    print("-" * 60)
    print("\nKernel for Vertical Line Detection:")
    print(kernel)
    Marvellous_Display(kernel, "Kernel")

    conv = Marvellous_Convolution_Animated(image, kernel, delay=1.0)
    Marvellous_Display(conv, "Final Convolution Output")

    relu = Marvellous_ReLU(conv)
    Marvellous_Display(relu, "ReLU Output")

    pool = Marvellous_Pooling_Animated(relu, delay=1.0)
    Marvellous_Display(pool, "Final Pooling Output")

    flat = Marvellous_Flatten(pool)
    score = Marvellous_FC(flat)

    print("\n" + "-" * 60)
    print("STEP 6 : FINAL PREDICTION")
    print("-" * 60)

    if score > 0:
        prediction = "Vertical Line"
    else:
        prediction = "Horizontal Line"

    print("\nActual Input     =", actual)
    print("Predicted Output =", prediction)

    Marvellous_ShowPipeline(image, conv, relu, pool)

if __name__ == "__main__" :
    Marvellous_CNN_Animated()