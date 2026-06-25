from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_employee_file():
    with open("/tmp/employees.txt", "w") as f:
        f.write("""Rahul,28
Priya,31
Amit,42
Sneha,26
Kiran,38""")

def calculate_average_age(ti):
    ages = []

    with open("/tmp/employees.txt") as f:
        for line in f:
            ages.append(int(line.strip().split(",")[1]))

    ti.xcom_push(key="youngest", value=min(ages))
    ti.xcom_push(key="oldest", value=max(ages))
    ti.xcom_push(key="average", value=sum(ages)/len(ages))

def generate_age_report(ti):
    youngest = ti.xcom_pull(task_ids="calculate_average_age", key="youngest")
    oldest = ti.xcom_pull(task_ids="calculate_average_age", key="oldest")
    average = ti.xcom_pull(task_ids="calculate_average_age", key="average")

    with open("/tmp/age_report.txt", "w") as f:
        f.write(
            f"Youngest Employee = {youngest}\n"
            f"Oldest Employee = {oldest}\n"
            f"Average Age = {average}"
        )

with DAG(
    dag_id="exercise13_employee_age_report",
    start_date=datetime(2025,1,1),
    schedule=None,
    catchup=False
) as dag:

    t1 = PythonOperator(task_id="create_employee_file", python_callable=create_employee_file)
    t2 = PythonOperator(task_id="calculate_average_age", python_callable=calculate_average_age)
    t3 = PythonOperator(task_id="generate_age_report", python_callable=generate_age_report)

    t1 >> t2 >> t3