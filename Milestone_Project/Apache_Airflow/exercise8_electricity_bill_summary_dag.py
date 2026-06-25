from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_bill_file():
    with open("/tmp/electricity.txt", "w") as f:
        f.write("""Rahul,210
Priya,180
Amit,300
Sneha,150
Kiran,260""")

def calculate_total_units(ti):
    total = 0
    count = 0

    with open("/tmp/electricity.txt") as f:
        for line in f:
            total += int(line.strip().split(",")[1])
            count += 1

    avg = total / count

    ti.xcom_push(key="total_units", value=total)
    ti.xcom_push(key="avg_units", value=avg)
    ti.xcom_push(key="customer_count", value=count)

def generate_bill_summary(ti):
    total = ti.xcom_pull(task_ids="calculate_total_units", key="total_units")
    avg = ti.xcom_pull(task_ids="calculate_total_units", key="avg_units")
    count = ti.xcom_pull(task_ids="calculate_total_units", key="customer_count")

    with open("/tmp/bill_summary.txt", "w") as f:
        f.write(
            f"Customers = {count}\n"
            f"Total Units = {total}\n"
            f"Average Units = {avg}"
        )

with DAG(
    dag_id="exercise8_electricity_bill_summary",
    start_date=datetime(2025,1,1),
    schedule=None,
    catchup=False
) as dag:

    t1 = PythonOperator(task_id="create_bill_file", python_callable=create_bill_file)
    t2 = PythonOperator(task_id="calculate_total_units", python_callable=calculate_total_units)
    t3 = PythonOperator(task_id="generate_bill_summary", python_callable=generate_bill_summary)

    t1 >> t2 >> t3