from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_file():
    with open("/tmp/message.txt", "w") as f:
        f.write("""Welcome to Apache Airflow
Learning DAGs
Learning Task Dependencies""")

def read_file():
    with open("/tmp/message.txt", "r") as f:
        print(f.read())

with DAG(
    dag_id="exercise1_file_read",
    start_date=datetime(2025,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="create_file",
        python_callable=create_file
    )

    t2 = PythonOperator(
        task_id="read_file",
        python_callable=read_file
    )

    t1 >> t2