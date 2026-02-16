from spark_session import get_spark_session
from pyspark.sql.functions import col

spark = get_spark_session()

# Load cleaned data
df = spark.read.csv("data/cleaned/sales_cleaned.csv", header=True, inferSchema=True)

# Add total_amount column
df = df.withColumn("total_amount", col("quantity") * col("price"))

# Save transformed data
df.write.mode("overwrite").parquet("data/analytics/spark_transformed")

print("PySpark transformations completed. Output saved to data/analytics/spark_transformed")
