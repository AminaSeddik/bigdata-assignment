# load.py
import pandas as pd
import sys

# Accept file path as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python load.py <path_to_csv_file>")
    sys.exit(1)

file_path = sys.argv[1]

# Load the dataset
df = pd.read_csv(file_path)

# Print basic information and the first few rows
print(df.info())
print(df.head())
