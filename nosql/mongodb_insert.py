from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.analytics_db
collection = db.product_summary

# Load analytics data
df = pd.read_csv("data/analytics/product_summary.csv")

# Convert dataframe to dictionary
records = df.to_dict(orient="records")

# Insert into MongoDB
collection.insert_many(records)

print("Inserted analytics summary into MongoDB successfully.")
