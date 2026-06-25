from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_result_file():
    with open("/tmp/results.txt", "w") as f:
        f.write("""Rahul,Pass
Priya,Fail
Amit,Pass
Sneha,Pass
Kiran,Fail
Megha,Pass""")

def count_pass_fail(ti):
    passed = 0
    failed = 0

    with open("/tmp/results.txt") as f:
        for line in f:
            status = line.strip().split(",")[1]

            if status == "Pass":
                passed += 1
            else:
                failed += 1

    ti.xcom_push(key="pass_count", value=passed)
    ti.xcom_push(key="fail_count", value=failed)

def generate_result_summary(ti):
    passed = ti.xcom_pull(task_ids="count_pass_fail", key="pass_count")
    failed = ti.xcom_pull(task_ids="count_pass_fail", key="fail_count")

    with open("/tmp/result_summary.txt", "w") as f:
        f.write(
            f"Total Pass = {passed}\n"
            f"Total Fail = {failed}"
        )

with DAG(
    dag_id="exercise9_exam_result_report",
    start_date=datetime(2025,1,1),
    schedule=None,
    catchup=False
) as dag:

    t1 = PythonOperator(task_id="create_result_file", python_callable=create_result_file)
    t2 = PythonOperator(task_id="count_pass_fail", python_callable=count_pass_fail)
    t3 = PythonOperator(task_id="generate_result_summary", python_callable=generate_result_summary)

    t1 >> t2 >> t3