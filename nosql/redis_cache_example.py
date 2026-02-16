import redis
import json
import pandas as pd

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Load analytics data
df = pd.read_csv("data/analytics/product_summary.csv")

# Convert to JSON
data_json = df.to_json(orient="records")

# Store in Redis cache
r.set("product_summary_cache", data_json)

# Retrieve from Redis
cached_data = r.get("product_summary_cache")
print("Cached Data:", json.loads(cached_data))
