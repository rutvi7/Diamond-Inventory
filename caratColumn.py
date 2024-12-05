import pandas as pd

# Load the dataset
FILE_PATH = "diamonds.csv"

try:
    # Read the dataset
    df = pd.read_csv(FILE_PATH)
    print(f"Dataset loaded successfully with {len(df)} rows.")
    
    # Check for the 'carat weight' column
    if 'carat_weight' not in df.columns:
        print("Error: 'carat_weight' column not found. Cannot calculate 'carat'.")
    else:
        # Calculate the 'carat' column using 'carat_weight'
        print("Calculating 'Carat' values using 'carat_weight'...")
        df['Carat'] = df['carat_weight']  # Copy values directly

        # Save the updated dataset
        UPDATED_FILE_PATH = "diamonds_updated.csv"
        df.to_csv(UPDATED_FILE_PATH, index=False)
        print(f"The updated dataset with the 'Carat' column has been saved as '{UPDATED_FILE_PATH}'.")

except FileNotFoundError:
    print("Error: The file was not found. Please check the file path.")
