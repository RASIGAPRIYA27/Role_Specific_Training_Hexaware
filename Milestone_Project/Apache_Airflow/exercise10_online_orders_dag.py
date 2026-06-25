from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import csv

def create_orders():
    with open("/tmp/orders.csv", "w") as f:
        f.write("""product,quantity,price
Laptop,1,70000
Mouse,4,500
Monitor,2,12000
Keyboard,3,1500""")

def calculate_order_value(ti):
    total_revenue = 0
    highest_product = ""
    highest_revenue = 0

    with open("/tmp/orders.csv") as f:
        reader = csv.DictReader(f)

        for row in reader:
            revenue = int(row["quantity"]) * int(row["price"])

            if revenue > highest_revenue:
                highest_revenue = revenue
                highest_product = row["product"]

            total_revenue += revenue

    ti.xcom_push(key="total_revenue", value=total_revenue)
    ti.xcom_push(key="highest_product", value=highest_product)

def generate_sales_report(ti):
    total = ti.xcom_pull(task_ids="calculate_order_value", key="total_revenue")
    product = ti.xcom_pull(task_ids="calculate_order_value", key="highest_product")

    with open("/tmp/sales_report.txt", "w") as f:
        f.write(
            f"Total Revenue = {total}\n"
            f"Highest Selling Product = {product}"
        )

with DAG(
    dag_id="exercise10_online_orders",
    start_date=datetime(2025,1,1),
    schedule=None,
    catchup=False
) as dag:

    t1 = PythonOperator(task_id="create_orders", python_callable=create_orders)
    t2 = PythonOperator(task_id="calculate_order_value", python_callable=calculate_order_value)
    t3 = PythonOperator(task_id="generate_sales_report", python_callable=generate_sales_report)

    t1 >> t2 >> t3