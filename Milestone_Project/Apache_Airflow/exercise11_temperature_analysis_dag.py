from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_temperature_file():
    with open("/tmp/temperature.txt", "w") as f:
        f.write("""Monday,34
Tuesday,36
Wednesday,31
Thursday,38
Friday,35
Saturday,33
Sunday,32""")

def find_highest_temperature(ti):
    temps = []

    with open("/tmp/temperature.txt") as f:
        for line in f:
            temps.append(int(line.strip().split(",")[1]))

    highest = max(temps)
    avg = sum(temps) / len(temps)

    ti.xcom_push(key="highest_temp", value=highest)
    ti.xcom_push(key="avg_temp", value=avg)

def generate_weather_report(ti):
    highest = ti.xcom_pull(task_ids="find_highest_temperature", key="highest_temp")
    avg = ti.xcom_pull(task_ids="find_highest_temperature", key="avg_temp")

    with open("/tmp/weather_report.txt", "w") as f:
        f.write(
            f"Highest Temperature = {highest}\n"
            f"Average Temperature = {avg}"
        )

with DAG(
    dag_id="exercise11_temperature_analysis",
    start_date=datetime(2025,1,1),
    schedule=None,
    catchup=False
) as dag:

    t1 = PythonOperator(task_id="create_temperature_file", python_callable=create_temperature_file)
    t2 = PythonOperator(task_id="find_highest_temperature", python_callable=find_highest_temperature)
    t3 = PythonOperator(task_id="generate_weather_report", python_callable=generate_weather_report)

    t1 >> t2 >> t3