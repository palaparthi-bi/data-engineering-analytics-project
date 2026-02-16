import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("data/cleaned/sales_cleaned.csv")

scaler = MinMaxScaler()
df["price_scaled"] = scaler.fit_transform(df[["price"]])

df.to_csv("data/cleaned/sales_preprocessed.csv", index=False)

print("Preprocessing completed. Preprocessed file saved to data/cleaned/")
