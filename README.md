# data-engineering-analytics-project
End-to-end data engineering project using Python, PySpark, SQL, Airflow, and NoSQL.

This project is something I built to practice real-world data engineering concepts.
It covers the full pipeline — from raw data all the way to analytics — using tools like Python, PySpark, SQL, Airflow, MongoDB, and Redis.

The goal was to simulate how data flows through a modern data platform and to get hands‑on experience with cleaning, transforming, storing, and orchestrating data.

---

**Tech Stack**
Python
PySpark
SQL (PostgreSQL/MySQL)
Apache Airflow
MongoDB
Redis
Git & GitHub

---
**What the Pipeline Does**
Cleans raw sales data
Preprocesses and scales fields
Runs PySpark transformations
Generates aggregated analytics
Stores results in SQL and NoSQL
Orchestrates everything with Airflow

**Folder Structure**

data/
python/
pyspark/
sql/
airflow/
nosql/
models/

**Data Model**
The project uses a simple star schema with:

fact_sales (transaction data)
dim_product (product details)
More details are in models/data_model.md

**How to Run**
Python scripts:
python3 python/data_cleaning.py
python3 python/preprocessing.py
python3 python/analytics.py

PySpark:
spark-submit pyspark/transformations.py
spark-submit pyspark/aggregations.py

Airflow:
Place the DAG in airflow/dags/


I’m Kishore, and I’m building this project to strengthen my data engineering skills and prepare for real-world roles involving Python, Spark, SQL, and cloud data pipelines.
