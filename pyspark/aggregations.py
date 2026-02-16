from spark_session import get_spark_session
from pyspark.sql.functions import sum, avg

spark = get_spark_session()

# Load transformed data
df = spark.read.parquet("data/analytics/spark_transformed")

# Aggregate analytics
agg_df = df.groupBy("product_id").agg(
    sum("quantity").alias("total_qty"),
    avg("price").alias("avg_price"),
    sum("total_amount").alias("total_revenue")
)

# Save analytics output
agg_df.write.mode("overwrite").parquet("data/analytics/spark_summary")

print("PySpark aggregations completed. Summary saved to data/analytics/spark_summary")
