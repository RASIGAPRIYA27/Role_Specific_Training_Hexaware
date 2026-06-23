from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_inventory():
    with open("/tmp/inventory.txt", "w") as f:
        f.write("""Rice,50
Oil,7
Soap,35
Sugar,10
Tea,5""")

def find_low_stock(ti):
    items = []

    with open("/tmp/inventory.txt") as f:
        for line in f:
            product, qty = line.strip().split(",")

            if int(qty) < 15:
                items.append(product)

    ti.xcom_push(key="low_stock", value=items)

def generate_alert(ti):
    products = ti.xcom_pull(
        task_ids="find_low_stock",
        key="low_stock"
    )

    with open("/tmp/alerts.txt", "w") as f:
        f.write("\n".join(products))

with DAG(
    dag_id="exercise4_stock_alert",
    start_date=datetime(2025,1,1),
    schedule=None,
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="create_inventory",
        python_callable=create_inventory
    )

    t2 = PythonOperator(
        task_id="find_low_stock",
        python_callable=find_low_stock
    )

    t3 = PythonOperator(
        task_id="generate_alert",
        python_callable=generate_alert
    )

    t1 >> t2 >> t3