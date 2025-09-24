import pandas as pd
import os

print("🚀 Hello, script is running")

# Create a sample dataframe with column names
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print('yes')

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ensure "data" directory exists in the same location as the script
data_dir = os.path.join(script_dir, "data")
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a csv file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
import os
print("🔍 Current working directory:", os.getcwd())
