# Steps for machine learning application 

# Step 1 : Data Gathering / Collection
# Step 2 : Data Analysis
# Step 3 : Data Cleaning
# Step 4 : Model Selection
# Step 5 : Model Training
# Step 6 : Model Testing / Evaluation
# Step 7 : Model Improvement
# Step 8 : Prediction / Deployment

import sklearn

def main():
    print("Ball Classification Case Study")

    # Data Loading 
    Features = [[35, "Rough"], [47, "Rough"], [90, "Smooth"], [48, "Rough"],[90, "Smooth"],
        [35, "Rough"], [92, "Smooth"], [35, "Rough"], [35, "Rough"], [35, "Rough"], [96, "Smooth"], [43, "Rough"],
        [110, "Smooth"], [35, "Rough"], [95, "Smooth"]] 
    Labels = ["Tennis", "Tennis", "Cricket", "Tennis", "Cricket", "Tennis", "Cricket", "Tennis"
              , "Tennis", "Tennis", "Cricket", "Tennis", "Cricket", "Tennis", "Cricket"]
    

if __name__ == "__main__":
    main()

# Dataset Size : 15