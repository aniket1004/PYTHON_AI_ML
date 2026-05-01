# ============================================================
# Project Name : AI-Based Financial Time Series Forecasting
# Stock        : Reliance Stock Sample Data
# Algorithm    : LSTM - Long Short-Term Memory
# ============================================================

"""
1. Dataset loading
2. Close price extraction
3. Manual Min-Max scaling calculation
4. Time-series sequence creation
5. Shape conversion required by LSTM
6. LSTM gate formulas and their purpose
7. Model architecture
8. Training process
9. Prediction process
10. Inverse scaling calculation
11. Error calculation: MAE, MSE, RMSE
12. Graph generation
13. Next-day stock price prediction
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping


# ------------------------------------------------------------
# Utility Function : Print Section Header
# ------------------------------------------------------------

def Marvellous_Header(title):
    print("\n" + "=" * 80)
    print(title.center(80))
    print("=" * 80)


# ------------------------------------------------------------
# Utility Function : Print Small Table
# ------------------------------------------------------------

def Display_Table(title, dataframe, rows=10):
    Marvellous_Header(title)
    print(dataframe.head(rows).to_string(index=False))


# ------------------------------------------------------------
# Step 1 : Load Dataset
# ------------------------------------------------------------

Marvellous_Header("MARVELLOUS INFOSYSTEMS - RELIANCE STOCK FORECASTING USING LSTM")

DATASET_PATH = "marvellous_reliance_stock_sample.csv"

if not os.path.exists(DATASET_PATH):
    raise FileNotFoundError(
        "Dataset not found. Please keep marvellous_reliance_stock_sample.csv in the same folder."
    )

data = pd.read_csv(DATASET_PATH)

Display_Table("STEP 1 : ORIGINAL DATASET VALUES", data, rows=12)

print("\nDataset Shape:", data.shape)
print("Total Rows   :", data.shape[0])
print("Total Columns:", data.shape[1])
print("Column Names :", list(data.columns))

print("\nDataset Data Types:")
print(data.dtypes)


# ------------------------------------------------------------
# Step 2 : Date Conversion and Sorting
# ------------------------------------------------------------

Marvellous_Header("STEP 2 : DATE CONVERSION AND SORTING")

print("Before conversion, Date column type:", data["Date"].dtype)

data["Date"] = pd.to_datetime(data["Date"])
data = data.sort_values("Date").reset_index(drop=True)

print("After conversion, Date column type :", data["Date"].dtype)
print("\nFirst Date in Dataset:", data["Date"].iloc[0].date())
print("Last Date in Dataset :", data["Date"].iloc[-1].date())


# ------------------------------------------------------------
# Step 3 : Select Close Price
# ------------------------------------------------------------

Marvellous_Header("STEP 3 : EXTRACT CLOSE PRICE FOR FORECASTING")

# We use only Close price for beginner-friendly time series forecasting.
# In advanced projects, Open, High, Low, Close, Volume and technical indicators can also be used.
close_prices = data[["Close"]].values

print("Close price values are extracted as a NumPy array.")
print("Shape of close_prices:", close_prices.shape)
print("\nFirst 10 Close Prices:")
for i in range(min(10, len(close_prices))):
    print(f"Day {i+1:02d} Close Price = {close_prices[i][0]}")


# ------------------------------------------------------------
# Step 4 : Manual Min-Max Scaling Demonstration
# ------------------------------------------------------------

Marvellous_Header("STEP 4 : MIN-MAX SCALING WITH MANUAL CALCULATION")

minimum_price = close_prices.min()
maximum_price = close_prices.max()

print("Minimum Close Price:", minimum_price)
print("Maximum Close Price:", maximum_price)

print("\nFormula of Min-Max Scaling:")
print("Scaled Value = (Original Value - Minimum Value) / (Maximum Value - Minimum Value)")

print("\nManual scaling calculation for first 5 records:")
for i in range(min(5, len(close_prices))):
    original = close_prices[i][0]
    scaled_manual = (original - minimum_price) / (maximum_price - minimum_price)
    print(
        f"Record {i+1}: ({original} - {minimum_price}) / "
        f"({maximum_price} - {minimum_price}) = {scaled_manual:.6f}"
    )

# Actual scaling using sklearn
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_close = scaler.fit_transform(close_prices)

print("\nFirst 10 scaled values produced by MinMaxScaler:")
for i in range(min(10, len(scaled_close))):
    print(f"Day {i+1:02d} Original = {close_prices[i][0]}  Scaled = {scaled_close[i][0]:.6f}")


# ------------------------------------------------------------
# Step 5 : Create Time Series Sequences
# ------------------------------------------------------------

Marvellous_Header("STEP 5 : TIME SERIES SEQUENCE CREATION")

TIME_STEPS = 10

print("TIME_STEPS =", TIME_STEPS)
print("Meaning: Previous 10 days are used to predict the next day.")
print("\nExample:")
print("Input  = Day 1 to Day 10 Close Prices")
print("Output = Day 11 Close Price")


def Create_Sequences(dataset, time_steps=10):
    X = []
    y = []

    for i in range(time_steps, len(dataset)):
        previous_days = dataset[i-time_steps:i, 0]
        next_day = dataset[i, 0]

        X.append(previous_days)
        y.append(next_day)

    return np.array(X), np.array(y)


X, y = Create_Sequences(scaled_close, TIME_STEPS)

print("\nTotal sequences created:", len(X))
print("Shape of X before reshape:", X.shape)
print("Shape of y:", y.shape)

print("\nFirst 3 sequences with scaled values:")
for seq_index in range(min(3, len(X))):
    print("\nSequence Number:", seq_index + 1)
    print("Input X values:")
    for day_index in range(TIME_STEPS):
        print(f"  Previous Day {day_index+1:02d}: {X[seq_index][day_index]:.6f}")
    print(f"Output y value: {y[seq_index]:.6f}")

print("\nSame first sequence in original price values:")
first_sequence_original = scaler.inverse_transform(X[0].reshape(-1, 1))
first_output_original = scaler.inverse_transform([[y[0]]])

for i, value in enumerate(first_sequence_original):
    print(f"Input Day {i+1:02d}: {value[0]:.2f}")
print("Output Next Day:", round(first_output_original[0][0], 2))


# ------------------------------------------------------------
# Step 6 : Reshape Input for LSTM
# ------------------------------------------------------------

Marvellous_Header("STEP 6 : RESHAPE DATA FOR LSTM INPUT")

print("LSTM expects 3D input:")
print("[Number of Samples, Number of Time Steps, Number of Features]")
print("\nIn our project:")
print("Samples    = Total number of sequences")
print("Time Steps = 10 previous days")
print("Features   = 1 because we use only Close price")

X = X.reshape(X.shape[0], X.shape[1], 1)

print("\nShape of X after reshape:", X.shape)
print("Shape meaning:", X.shape[0], "samples,", X.shape[1], "time steps,", X.shape[2], "feature")


# ------------------------------------------------------------
# Step 7 : LSTM Concept and Gate Explanation
# ------------------------------------------------------------

Marvellous_Header("STEP 7 : LSTM INTERNAL WORKING CONCEPT")

print("LSTM is an improved version of RNN.")
print("It is useful for sequential data like stock prices, text, weather, sales, etc.")
print("\nLSTM maintains two important states:")
print("1. Hidden State h_t  : Short-term output information")
print("2. Cell State C_t    : Long-term memory information")

print("\nLSTM contains four main calculations:")
print("1. Forget Gate     : Decides what old memory should be forgotten")
print("2. Input Gate      : Decides what new information should be accepted")
print("3. Candidate Memory: Creates possible new memory")
print("4. Output Gate     : Decides current output hidden state")

print("\nMathematical Formulas:")
print("Forget Gate      f_t = sigmoid(W_f * [h_(t-1), x_t] + b_f)")
print("Input Gate       i_t = sigmoid(W_i * [h_(t-1), x_t] + b_i)")
print("Candidate Memory C~t = tanh(W_c * [h_(t-1), x_t] + b_c)")
print("Cell State       C_t = f_t * C_(t-1) + i_t * C~t")
print("Output Gate      o_t = sigmoid(W_o * [h_(t-1), x_t] + b_o)")
print("Hidden State     h_t = o_t * tanh(C_t)")


# ------------------------------------------------------------
# Step 8 : Manual Mini LSTM Gate Demonstration
# ------------------------------------------------------------

Marvellous_Header("STEP 8 : SIMPLE MANUAL LSTM GATE CALCULATION DEMO")

print("Simplified calculation")
print("Actual Keras LSTM uses many weights and matrix operations internally.")

# One input value from first sequence
x_t = float(X[0][0][0])
h_previous = 0.0
C_previous = 0.0

# Simple manually selected weights for demonstration
Wf, bf = 0.7, 0.1
Wi, bi = 0.6, 0.2
Wc, bc = 0.5, 0.0
Wo, bo = 0.8, 0.1


def sigmoid(z):
    return 1 / (1 + np.exp(-z))

forget_gate = sigmoid(Wf * x_t + bf)
input_gate = sigmoid(Wi * x_t + bi)
candidate_memory = np.tanh(Wc * x_t + bc)
cell_state = forget_gate * C_previous + input_gate * candidate_memory
output_gate = sigmoid(Wo * x_t + bo)
hidden_state = output_gate * np.tanh(cell_state)

print("Input value x_t:", round(x_t, 6))
print("Previous hidden state h_previous:", h_previous)
print("Previous cell state C_previous  :", C_previous)

print("\nForget Gate Calculation:")
print(f"f_t = sigmoid(({Wf} * {x_t:.6f}) + {bf}) = {forget_gate:.6f}")

print("\nInput Gate Calculation:")
print(f"i_t = sigmoid(({Wi} * {x_t:.6f}) + {bi}) = {input_gate:.6f}")

print("\nCandidate Memory Calculation:")
print(f"C_candidate = tanh(({Wc} * {x_t:.6f}) + {bc}) = {candidate_memory:.6f}")

print("\nNew Cell State Calculation:")
print(f"C_t = ({forget_gate:.6f} * {C_previous}) + ({input_gate:.6f} * {candidate_memory:.6f}) = {cell_state:.6f}")

print("\nOutput Gate Calculation:")
print(f"o_t = sigmoid(({Wo} * {x_t:.6f}) + {bo}) = {output_gate:.6f}")

print("\nHidden State Calculation:")
print(f"h_t = {output_gate:.6f} * tanh({cell_state:.6f}) = {hidden_state:.6f}")


# ------------------------------------------------------------
# Step 9 : Train Test Split
# ------------------------------------------------------------

Marvellous_Header("STEP 9 : TRAIN TEST SPLIT")

train_size = int(len(X) * 0.80)

X_train = X[:train_size]
X_test = X[train_size:]
y_train = y[:train_size]
y_test = y[train_size:]

print("Total Records after sequence creation:", len(X))
print("Training Records 80%:", len(X_train))
print("Testing Records 20% :", len(X_test))

print("\nTraining X shape:", X_train.shape)
print("Training y shape:", y_train.shape)
print("Testing X shape :", X_test.shape)
print("Testing y shape :", y_test.shape)


# ------------------------------------------------------------
# Step 10 : Build LSTM Model
# ------------------------------------------------------------

Marvellous_Header("STEP 10 : BUILD LSTM MODEL")

model = Sequential()

# return_sequences=True is required because another LSTM layer is connected after this layer.
model.add(LSTM(units=50, return_sequences=True, input_shape=(TIME_STEPS, 1)))
model.add(Dropout(0.2))

# Last LSTM layer returns only final output, so return_sequences=False.
model.add(LSTM(units=50, return_sequences=False))
model.add(Dropout(0.2))

# Dense layer performs final decision-making / regression mapping.
model.add(Dense(units=25, activation="relu"))

# Output layer has one neuron because we predict one value: next Close price.
model.add(Dense(units=1))

model.compile(optimizer="adam", loss="mean_squared_error")

print("Model is compiled using:")
print("Optimizer : Adam")
print("Loss      : Mean Squared Error")
print("\nModel Summary:")
model.summary()

print("\nLayer Explanation:")
print("LSTM Layer 1  : Reads sequence of 10 days and returns sequence output")
print("Dropout 1     : Reduces overfitting by ignoring 20% neurons randomly")
print("LSTM Layer 2  : Learns final temporal pattern")
print("Dropout 2     : Again reduces overfitting")
print("Dense 25      : Learns nonlinear combination of LSTM output")
print("Dense 1       : Predicts next day scaled close price")


# ------------------------------------------------------------
# Step 11 : Train Model
# ------------------------------------------------------------

Marvellous_Header("STEP 11 : MODEL TRAINING")

print("During training, model compares predicted value with actual value.")
print("Then it updates internal weights using backpropagation through time.")
print("\nEpoch means one complete pass over training data.")
print("Batch size means number of samples processed before weight update.")

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=10,
    restore_best_weights=True
)

history = model.fit(
    X_train,
    y_train,
    epochs=60,
    batch_size=16,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=1
)

print("\nTraining completed.")
print("Total epochs actually executed:", len(history.history["loss"]))
print("Final training loss  :", history.history["loss"][-1])
print("Final validation loss:", history.history["val_loss"][-1])


# ------------------------------------------------------------
# Step 12 : Prediction on Test Data
# ------------------------------------------------------------

Marvellous_Header("STEP 12 : PREDICTION ON TEST DATA")

predicted_scaled = model.predict(X_test)

print("Predicted values are currently scaled between 0 and 1.")
print("\nFirst 10 scaled predictions vs actual scaled values:")
for i in range(min(10, len(predicted_scaled))):
    print(
        f"Record {i+1:02d}: Actual Scaled = {y_test[i]:.6f}, "
        f"Predicted Scaled = {predicted_scaled[i][0]:.6f}"
    )


# ------------------------------------------------------------
# Step 13 : Inverse Scaling
# ------------------------------------------------------------

Marvellous_Header("STEP 13 : CONVERT SCALED VALUES BACK TO ORIGINAL PRICE")

predicted_prices = scaler.inverse_transform(predicted_scaled)
actual_prices = scaler.inverse_transform(y_test.reshape(-1, 1))

print("Formula of inverse scaling:")
print("Original Value = Scaled Value * (Maximum - Minimum) + Minimum")

print("\nManual inverse scaling for first prediction:")
first_scaled_prediction = predicted_scaled[0][0]
manual_original_prediction = first_scaled_prediction * (maximum_price - minimum_price) + minimum_price
print(
    f"Original = {first_scaled_prediction:.6f} * "
    f"({maximum_price} - {minimum_price}) + {minimum_price} = {manual_original_prediction:.2f}"
)

print("\nFirst 10 predictions in original rupee value:")
for i in range(min(10, len(predicted_prices))):
    print(
        f"Record {i+1:02d}: Actual Price = {actual_prices[i][0]:.2f}, "
        f"Predicted Price = {predicted_prices[i][0]:.2f}, "
        f"Difference = {actual_prices[i][0] - predicted_prices[i][0]:.2f}"
    )


# ------------------------------------------------------------
# Step 14 : Error Calculation
# ------------------------------------------------------------

Marvellous_Header("STEP 14 : MODEL EVALUATION WITH CALCULATIONS")

mae = mean_absolute_error(actual_prices, predicted_prices)
mse = mean_squared_error(actual_prices, predicted_prices)
rmse = np.sqrt(mse)

print("MAE  = Mean of absolute differences")
print("MSE  = Mean of squared differences")
print("RMSE = Square root of MSE")

print("\nManual error calculation for first 5 records:")
absolute_errors = []
squared_errors = []

for i in range(min(5, len(actual_prices))):
    actual = actual_prices[i][0]
    predicted = predicted_prices[i][0]
    error = actual - predicted
    absolute_error = abs(error)
    squared_error = error ** 2
    absolute_errors.append(absolute_error)
    squared_errors.append(squared_error)

    print(
        f"Record {i+1}: Actual={actual:.2f}, Predicted={predicted:.2f}, "
        f"Error={error:.2f}, Absolute Error={absolute_error:.2f}, "
        f"Squared Error={squared_error:.2f}"
    )

print("\nFinal Evaluation on Complete Test Data:")
print("Mean Absolute Error :", round(mae, 2))
print("Mean Squared Error  :", round(mse, 2))
print("Root MSE            :", round(rmse, 2))


# ------------------------------------------------------------
# Step 15 : Visualization - Actual vs Predicted
# ------------------------------------------------------------

Marvellous_Header("STEP 15 : ACTUAL VS PREDICTED GRAPH")

plt.figure(figsize=(12, 6))
plt.plot(actual_prices, label="Actual Reliance Close Price")
plt.plot(predicted_prices, label="Predicted Reliance Close Price")
plt.title("Reliance Stock Price Forecasting using LSTM")
plt.xlabel("Test Record Number")
plt.ylabel("Close Price")
plt.legend()
plt.grid(True)
plt.savefig("marvellous_actual_vs_predicted_detailed.png")
plt.show()

print("Graph saved as marvellous_actual_vs_predicted_detailed.png")


# ------------------------------------------------------------
# Step 16 : Visualization - Training Loss
# ------------------------------------------------------------

Marvellous_Header("STEP 16 : TRAINING LOSS GRAPH")

plt.figure(figsize=(10, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Marvellous LSTM Training Loss")
plt.xlabel("Epoch Number")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.savefig("marvellous_training_loss_detailed.png")
plt.show()

print("Graph saved as marvellous_training_loss_detailed.png")


# ------------------------------------------------------------
# Step 17 : Predict Next Day Close Price
# ------------------------------------------------------------

Marvellous_Header("STEP 17 : NEXT DAY PRICE PREDICTION")

last_10_days = scaled_close[-TIME_STEPS:]

print("Last 10 days used for next-day prediction:")
last_10_original = scaler.inverse_transform(last_10_days)
for i in range(TIME_STEPS):
    print(
        f"Day {i+1:02d}: Original = {last_10_original[i][0]:.2f}, "
        f"Scaled = {last_10_days[i][0]:.6f}"
    )

last_10_days = last_10_days.reshape(1, TIME_STEPS, 1)
next_day_scaled = model.predict(last_10_days)
next_day_price = scaler.inverse_transform(next_day_scaled)

print("\nNext Day Prediction:")
print("Predicted Scaled Value:", round(float(next_day_scaled[0][0]), 6))
print("Predicted Original Close Price:", round(float(next_day_price[0][0]), 2))


# ------------------------------------------------------------
# Step 18 : Save Model and Output CSV
# ------------------------------------------------------------

Marvellous_Header("STEP 18 : SAVE MODEL AND PREDICTION OUTPUT")

model.save("marvellous_reliance_lstm_detailed_model.h5")

output_df = pd.DataFrame({
    "Actual_Close_Price": actual_prices.flatten(),
    "Predicted_Close_Price": predicted_prices.flatten(),
    "Difference": (actual_prices.flatten() - predicted_prices.flatten())
})

output_df.to_csv("marvellous_reliance_prediction_output.csv", index=False)

print("Model saved as marvellous_reliance_lstm_detailed_model.h5")
print("Prediction output saved as marvellous_reliance_prediction_output.csv")