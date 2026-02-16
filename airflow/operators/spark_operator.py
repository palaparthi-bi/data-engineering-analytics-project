from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import subprocess

class SparkSubmitOperator(BaseOperator):

    @apply_defaults
    def __init__(self, script_path, *args, **kwargs):
        super(SparkSubmitOperator, self).__init__(*args, **kwargs)
        self.script_path = script_path

    def execute(self, context):
        command = f"spark-submit {self.script_path}"
        subprocess.run(command, shell=True, check=True)
        print(f"Spark job executed: {self.script_path}")
