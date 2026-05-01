import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Function to print separator
# ------------------------------------------------------------
def Marvellous_Line():
    print("\n" + "-" * 70)

# ------------------------------------------------------------
# Function to display matrix graphically with values
# ------------------------------------------------------------
def Marvellous_Display(matrix, title, cmap='gray'):
    plt.figure(figsize=(5, 5))
    plt.imshow(matrix, cmap=cmap, interpolation='nearest')
    plt.title(title)
    plt.colorbar()

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            plt.text(j, i, f"{matrix[i][j]:.1f}",
                     ha='center', va='center',
                     color='red', fontsize=11)

    plt.show()

# ------------------------------------------------------------
# Function to display region and multiplication side by side
# ------------------------------------------------------------
def Marvellous_Display_Region(region, kernel, multiplication, title):
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))

    matrices = [region, kernel, multiplication]
    titles = ["Selected Region", "Kernel", "Region × Kernel"]

    for index in range(3):
        axes[index].imshow(matrices[index], cmap='gray', interpolation='nearest')
        axes[index].set_title(titles[index])

        for i in range(matrices[index].shape[0]):
            for j in range(matrices[index].shape[1]):
                axes[index].text(j, i, f"{matrices[index][i][j]:.1f}",
                                 ha='center', va='center',
                                 color='red', fontsize=11)

    plt.suptitle(title)
    plt.show()

# ------------------------------------------------------------
# Function : Convolution with full detailed calculations
# ------------------------------------------------------------
def Marvellous_Convolution(image, kernel):
    rows, cols = image.shape
    krows, kcols = kernel.shape

    output_rows = rows - krows + 1
    output_cols = cols - kcols + 1

    output = np.zeros((output_rows, output_cols))

    Marvellous_Line()
    print("STEP 1 : CONVOLUTION LAYER")
    Marvellous_Line()

    for i in range(output_rows):
        for j in range(output_cols):
            region = image[i:i+krows, j:j+kcols]
            multiplication = region * kernel
            result = np.sum(multiplication)

            output[i][j] = result

            print(f"\nPosition -> Row: {i}, Column: {j}")
            print("\nSelected Region:")
            print(region)

            print("\nKernel:")
            print(kernel)

            print("\nRegion × Kernel:")
            print(multiplication)

            print("\nCalculation:")
            flat_region = region.flatten()
            flat_kernel = kernel.flatten()
            terms = [f"({flat_region[x]:.0f}×{flat_kernel[x]:.0f})" for x in range(len(flat_region))]
            print(" + ".join(terms))

            print("\nSum =", result)

            Marvellous_Display_Region(
                region,
                kernel,
                multiplication,
                f"Convolution Step -> Position ({i},{j}) | Sum = {result:.1f}"
            )

    print("\nFinal Convolution Output:")
    print(output)

    return output

# ------------------------------------------------------------
# Function : ReLU activation
# ------------------------------------------------------------
def Marvellous_ReLU(data):
    Marvellous_Line()
    print("STEP 2 : RELU ACTIVATION")
    Marvellous_Line()

    output = np.maximum(0, data)

    print("\nInput to ReLU:")
    print(data)

    print("\nRule : ReLU(x) = max(0, x)")

    print("\nDetailed ReLU Conversion:")
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            print(f"ReLU({data[i][j]:.1f}) = {output[i][j]:.1f}")

    print("\nOutput after ReLU:")
    print(output)

    return output

# ------------------------------------------------------------
# Function : Max Pooling with graphics
# ------------------------------------------------------------
def Marvellous_Pooling(data, pool_size=2, stride=2):
    rows, cols = data.shape

    output_rows = ((rows - pool_size) // stride) + 1
    output_cols = ((cols - pool_size) // stride) + 1

    output = np.zeros((output_rows, output_cols))

    Marvellous_Line()
    print("STEP 3 : MAX POOLING")
    Marvellous_Line()

    out_i = 0
    for i in range(0, rows - pool_size + 1, stride):
        out_j = 0
        for j in range(0, cols - pool_size + 1, stride):
            block = data[i:i+pool_size, j:j+pool_size]
            max_value = np.max(block)
            output[out_i][out_j] = max_value

            print(f"\nPooling Block -> Output Position ({out_i},{out_j})")
            print(block)
            print("Maximum value selected =", max_value)

            Marvellous_Display(block, f"Pooling Block ({out_i},{out_j}) | Max = {max_value:.1f}")

            out_j += 1
        out_i += 1

    print("\nFinal Pooling Output:")
    print(output)

    return output

# ------------------------------------------------------------
# Function : Flatten
# ------------------------------------------------------------
def Marvellous_Flatten(data):
    Marvellous_Line()
    print("STEP 4 : FLATTEN LAYER")
    Marvellous_Line()

    flat = data.flatten()

    print("\nInput Matrix:")
    print(data)

    print("\nFlattened Vector:")
    print(flat)

    print("\nDetailed Flatten Mapping:")
    index = 0
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            print(f"Index {index} -> data[{i}][{j}] = {data[i][j]:.1f}")
            index += 1

    return flat

# ------------------------------------------------------------
# This function graphically displays:
# Flatten Layer
# Fully Connected Layer
# Output Layer
# ------------------------------------------------------------

def Marvellous_Display_Neural_Network(flat_data, weights, bias, score, prediction):

    import matplotlib.pyplot as plt
    import numpy as np

    input_count = len(flat_data)

    # Create figure
    plt.figure(figsize=(14,8))
    plt.title("Flatten Layer → Fully Connected Layer → Output Layer", fontsize=16)

    # --------------------------------------------------------
    # Flatten Layer Nodes
    # --------------------------------------------------------
    input_x = 1
    input_y_positions = np.linspace(1, 9, input_count)

    for i in range(input_count):
        plt.scatter(input_x, input_y_positions[i], s=1500, color='skyblue')
        plt.text(input_x, input_y_positions[i],
                 f"F{i+1}\n{flat_data[i]:.1f}",
                 ha='center', va='center', fontsize=10)

    # --------------------------------------------------------
    # FC Layer Node
    # --------------------------------------------------------
    hidden_x = 5
    hidden_y = 5

    plt.scatter(hidden_x, hidden_y, s=2500, color='lightgreen')
    plt.text(hidden_x, hidden_y,
             f"Σ(WX)+B\n{score:.2f}",
             ha='center', va='center', fontsize=11)

    # --------------------------------------------------------
    # Output Node
    # --------------------------------------------------------
    output_x = 9
    output_y = 5

    plt.scatter(output_x, output_y, s=3000, color='orange')
    plt.text(output_x, output_y,
             f"Prediction\n{prediction}",
             ha='center', va='center', fontsize=11)

    # --------------------------------------------------------
    # Draw Connections Input → FC
    # --------------------------------------------------------
    for i in range(input_count):
        plt.plot([input_x+0.3, hidden_x-0.6],
                 [input_y_positions[i], hidden_y],
                 linewidth=1.5)

        mid_x = (input_x + hidden_x) / 2
        mid_y = (input_y_positions[i] + hidden_y) / 2

        plt.text(mid_x, mid_y,
                 f"W={weights[i]:.1f}",
                 fontsize=8, color='red')

    # --------------------------------------------------------
    # FC → Output
    # --------------------------------------------------------
    plt.plot([hidden_x+0.8, output_x-0.8],
             [hidden_y, output_y],
             linewidth=2)

    # --------------------------------------------------------
    # Bias Text
    # --------------------------------------------------------
    plt.text(hidden_x, hidden_y-1.5,
             f"Bias = {bias:.1f}",
             ha='center', fontsize=10, color='blue')

    # --------------------------------------------------------
    # Labels
    # --------------------------------------------------------
    plt.text(input_x, 9.8, "Flatten Layer", ha='center', fontsize=12)
    plt.text(hidden_x, 9.8, "Fully Connected", ha='center', fontsize=12)
    plt.text(output_x, 9.8, "Output Layer", ha='center', fontsize=12)

    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.axis('off')
    plt.show()

# ------------------------------------------------------------
# Function : Fully Connected Layer
# ------------------------------------------------------------
def Marvellous_FC(flat_data):

    Marvellous_Line()
    print("STEP 5 : FULLY CONNECTED LAYER")
    Marvellous_Line()

    # Dynamic weights
    weights = np.ones(len(flat_data), dtype=float)
    bias = -1.0

    print("\nFlatten Input:")
    print(flat_data)

    print("\nWeights:")
    print(weights)

    print("\nBias:")
    print(bias)

    multiplication = flat_data * weights
    result = np.sum(multiplication) + bias

    print("\nInput × Weights:")
    print(multiplication)

    print("\nDetailed FC Calculation:")
    terms = [f"({flat_data[i]:.1f}×{weights[i]:.1f})" for i in range(len(flat_data))]
    print(" + ".join(terms) + f" + ({bias})")

    print("\nSum of weighted inputs =", np.sum(multiplication))
    print("Final Output after adding bias =", result)

    # Prediction
    if result > 0:
        prediction = "Vertical Line"
    else:
        prediction = "Horizontal Line"

    # Graphical Network Display
    Marvellous_Display_Neural_Network(
        flat_data,
        weights,
        bias,
        result,
        prediction
    )

    return result

# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
def Marvellous_CNN_Demo():
    print("Choose Input Image")
    print("1 : Vertical Line")
    print("2 : Horizontal Line")

    choice = int(input("Enter your choice : "))

    # --------------------------------------------------------
    # Bigger 6x6 images
    # --------------------------------------------------------
    if choice == 1:
        image = np.array([
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0]
        ], dtype=float)
        actual = "Vertical Line"

    else:
        image = np.array([
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ], dtype=float)
        actual = "Horizontal Line"

    Marvellous_Line()
    print("INPUT IMAGE")
    Marvellous_Line()
    print("\nActual Input =", actual)
    print("\nInput Matrix:")
    print(image)
    Marvellous_Display(image, "Input Image")

    # --------------------------------------------------------
    # Kernel for vertical pattern detection
    # --------------------------------------------------------
    kernel = np.array([
        [-1,  1,  1, -1],
        [-1,  1,  1, -1],
        [-1,  1,  1, -1]
    ], dtype=float)

    Marvellous_Line()
    print("KERNEL")
    Marvellous_Line()
    print("\nKernel used to detect vertical features:")
    print(kernel)
    Marvellous_Display(kernel, "Vertical Detection Kernel")

    # --------------------------------------------------------
    # Step 1 : Convolution
    # --------------------------------------------------------
    conv = Marvellous_Convolution(image, kernel)
    Marvellous_Display(conv, "Convolution Output")

    # --------------------------------------------------------
    # Step 2 : ReLU
    # --------------------------------------------------------
    relu = Marvellous_ReLU(conv)
    Marvellous_Display(relu, "ReLU Output")

    # --------------------------------------------------------
    # Step 3 : Max Pooling
    # --------------------------------------------------------
    pool = Marvellous_Pooling(relu, pool_size=2, stride=1)
    Marvellous_Display(pool, "Pooling Output")

    # --------------------------------------------------------
    # Step 4 : Flatten
    # --------------------------------------------------------
    flat = Marvellous_Flatten(pool)

    # --------------------------------------------------------
    # Step 5 : Fully Connected Layer
    # --------------------------------------------------------
    score = Marvellous_FC(flat)

    # --------------------------------------------------------
    # Step 6 : Final Prediction
    # --------------------------------------------------------
    Marvellous_Line()
    print("STEP 6 : FINAL PREDICTION")
    Marvellous_Line()

    print("\nFinal Score =", score)

    if score > 0:
        prediction = "Vertical Line"
    else:
        prediction = "Horizontal Line"

    print("\nPredicted Output =", prediction)
    print("Actual Input      =", actual)

if __name__ == "__main__" :
    Marvellous_CNN_Demo()