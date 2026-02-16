import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/sales.csv")

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna(0, inplace=True)

# Add a calculated column
df["total_amount"] = df["quantity"] * df["price"]

# Save cleaned data
df.to_csv("data/cleaned/sales_cleaned.csv", index=False)

print("Data cleaning completed. Cleaned file saved to data/cleaned/")
