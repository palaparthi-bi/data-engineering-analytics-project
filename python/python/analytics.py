import pandas as pd

df = pd.read_csv("data/cleaned/sales_preprocessed.csv")

summary = df.groupby("product_id").agg({
    "quantity": "sum",
    "total_amount": "sum",
    "price": "mean",
    "price_scaled": "mean"
}).reset_index()

summary.to_csv("data/analytics/product_summary.csv", index=False)

print("Analytics completed. Summary saved to data/analytics/")
