from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "kishore",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

with DAG(
    dag_id="daily_etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
):

    # Step 1: Clean raw data using Python
    clean_data = BashOperator(
        task_id="clean_data",
        bash_command="python3 python/data_cleaning.py"
    )

    # Step 2: Preprocess data
    preprocess_data = BashOperator(
        task_id="preprocess_data",
        bash_command="python3 python/preprocessing.py"
    )

    # Step 3: Run PySpark transformations
    spark_transform = BashOperator(
        task_id="spark_transform",
        bash_command="spark-submit pyspark/transformations.py"
    )

    # Step 4: Run PySpark aggregations
    spark_aggregate = BashOperator(
        task_id="spark_aggregate",
        bash_command="spark-submit pyspark/aggregations.py"
    )

    clean_data >> preprocess_data >> spark_transform >> spark_aggregate
