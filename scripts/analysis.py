# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set Seaborn style for visualizations
sns.set(style="whitegrid")

# Define paths for data and output
data_path = "../data/CloudWatch_Traffic_Web_Attack_Cleaned.csv"
images_path = "../images"

# Ensure the output directory for images exists
os.makedirs(images_path, exist_ok=True)

# Load and analyze the dataset
print("Loading cleaned dataset...")
data = pd.read_csv(data_path)
print(f"Dataset loaded successfully!\nShape of the dataset: {data.shape}\n")
print("First few rows of the dataset:")
print(data.head())

# Analyze the distribution of 'bytes_in'
print("\nAnalyzing 'bytes_in' distribution...")
plt.figure(figsize=(10, 6))
sns.histplot(data['bytes_in'], bins=30, kde=True, color='blue')
plt.title('Distribution of Bytes In')
plt.xlabel('Bytes In')
plt.ylabel('Frequency')
plt.tight_layout()
bytes_in_dist_path = os.path.join(images_path, "bytes_in_distribution.png")
plt.savefig(bytes_in_dist_path)
print(f"Histogram saved as {bytes_in_dist_path}")
plt.close()

# Analyze the relationship between 'bytes_in' and 'bytes_out'
print("\nAnalyzing relationship between 'bytes_in' and 'bytes_out'...")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='bytes_in', y='bytes_out', data=data, alpha=0.6)
plt.title('Bytes In vs. Bytes Out')
plt.xlabel('Bytes In')
plt.ylabel('Bytes Out')
plt.tight_layout()
bytes_in_out_scatter_path = os.path.join(images_path, "bytes_in_vs_bytes_out.png")
plt.savefig(bytes_in_out_scatter_path)
print(f"Scatter plot saved as {bytes_in_out_scatter_path}")
plt.close()

# Analyze detection types
print("\nAnalyzing detection types...")
plt.figure(figsize=(10, 6))
sns.countplot(
    data=data,
    y='detection_types',
    order=data['detection_types'].value_counts().index,
    palette='viridis',  # Assigning a palette
    dodge=False  # Ensures no legend unless explicitly needed
)
plt.title('Detection Types Count')
plt.xlabel('Count')
plt.ylabel('Detection Types')
plt.tight_layout()

# Save the visualization
detection_types_path = os.path.join(images_path, "detection_types_count.png")
plt.savefig(detection_types_path)
print(f"Bar plot saved as {detection_types_path}")
plt.close()

print("\nAnalysis and visualization completed successfully.")
