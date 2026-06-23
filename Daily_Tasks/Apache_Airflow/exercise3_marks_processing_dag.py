from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_marks_file():
    with open("/tmp/marks.txt", "w") as f:
        f.write("""Math,80
Science,75
English,90
Python,95""")

def calculate_average(ti):
    total = 0
    count = 0

    with open("/tmp/marks.txt") as f:
        for line in f:
            total += int(line.strip().split(",")[1])
            count += 1

    avg = total / count

    ti.xcom_push(key="avg_marks", value=avg)

def generate_result(ti):
    avg = ti.xcom_pull(
        task_ids="calculate_average",
        key="avg_marks"
    )

    result = "PASS" if avg >= 50 else "FAIL"

    with open("/tmp/result.txt", "w") as f:
        f.write(
            f"Average Marks = {avg}\n"
            f"Result = {result}"
        )

with DAG(
    dag_id="exercise3_marks_processing",
    start_date=datetime(2025,1,1),
    schedule=None,
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="create_marks_file",
        python_callable=create_marks_file
    )

    t2 = PythonOperator(
        task_id="calculate_average",
        python_callable=calculate_average
    )

    t3 = PythonOperator(
        task_id="generate_result",
        python_callable=generate_result
    )

    t1 >> t2 >> t3