from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_attendance():
    with open("/tmp/attendance.txt", "w") as f:
        f.write("""Rahul,Present
Priya,Present
Amit,Absent
Sneha,Present
Kiran,Absent""")

def count_present(ti):
    present = 0

    with open("/tmp/attendance.txt") as f:
        for line in f:
            if "Present" in line:
                present += 1

    ti.xcom_push(key="present", value=present)

def count_absent(ti):
    absent = 0

    with open("/tmp/attendance.txt") as f:
        for line in f:
            if "Absent" in line:
                absent += 1

    ti.xcom_push(key="absent", value=absent)

def generate_summary(ti):
    present = ti.xcom_pull(
        task_ids="count_present",
        key="present"
    )

    absent = ti.xcom_pull(
        task_ids="count_absent",
        key="absent"
    )

    with open("/tmp/attendance_report.txt", "w") as f:
        f.write(
            f"Total Students = 5\n"
            f"Present = {present}\n"
            f"Absent = {absent}"
        )

with DAG(
    dag_id="exercise5_attendance_report",
    start_date=datetime(2025,1,1),
    schedule=None,
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="create_attendance",
        python_callable=create_attendance
    )

    t2 = PythonOperator(
        task_id="count_present",
        python_callable=count_present
    )

    t3 = PythonOperator(
        task_id="count_absent",
        python_callable=count_absent
    )

    t4 = PythonOperator(
        task_id="generate_summary",
        python_callable=generate_summary
    )

    t1 >> [t2, t3] >> t4