import pandas as pd

# Step 1: Define the path to the dataset
data_path = "../data/CloudWatch_Traffic_Web_Attack.csv"

try:
    # Step 2: Load the dataset
    print("Loading dataset...")
    data = pd.read_csv(data_path)

    # Step 3: Display basic information about the dataset
    print("Dataset loaded successfully!")
    print(f"Shape of the dataset: {data.shape}")
    print("First few rows of the dataset:")
    print(data.head())

    # Step 4: Save a cleaned version (if needed)
    # Remove rows with missing values (optional)
    data_cleaned = data.dropna()
    cleaned_path = "../data/CloudWatch_Traffic_Web_Attack_Cleaned.csv"
    data_cleaned.to_csv(cleaned_path, index=False)
    print(f"Cleaned dataset saved to {cleaned_path}")
except FileNotFoundError:
    print(f"Error: {data_path} not found. Please ensure the dataset is in the 'data' folder.")
