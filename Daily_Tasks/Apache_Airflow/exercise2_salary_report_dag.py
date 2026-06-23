from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_salary_file():
    with open("/tmp/employees.txt", "w") as f:
        f.write("""Rahul,45000
Priya,52000
Amit,61000
Sneha,48000""")

def calculate_total_salary(ti):
    total = 0

    with open("/tmp/employees.txt") as f:
        for line in f:
            total += int(line.strip().split(",")[1])

    ti.xcom_push(key="total_salary", value=total)

def generate_report(ti):
    total = ti.xcom_pull(
        task_ids="calculate_total_salary",
        key="total_salary"
    )

    with open("/tmp/report.txt", "w") as f:
        f.write(
            f"Salary Report\n"
            f"Employees = 4\n"
            f"Total Salary = {total}"
        )

with DAG(
    dag_id="exercise2_salary_report",
    start_date=datetime(2025,1,1),
    schedule=None,
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="create_salary_file",
        python_callable=create_salary_file
    )

    t2 = PythonOperator(
        task_id="calculate_total_salary",
        python_callable=calculate_total_salary
    )

    t3 = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report
    )

    t1 >> t2 >> t3