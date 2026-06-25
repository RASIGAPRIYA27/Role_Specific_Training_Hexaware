from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_enrollment_file():
    with open("/tmp/enrollments.txt", "w") as f:
        f.write("""Python,Rahul
Python,Priya
SQL,Amit
Python,Sneha
Power BI,Kiran
SQL,Megha
Power BI,Arjun""")

def count_students(ti):
    course_count = {}

    with open("/tmp/enrollments.txt") as f:
        for line in f:
            course = line.strip().split(",")[0]
            course_count[course] = course_count.get(course, 0) + 1

    ti.xcom_push(key="course_count", value=course_count)

def generate_course_report(ti):
    course_count = ti.xcom_pull(
        task_ids="count_students",
        key="course_count"
    )

    with open("/tmp/course_report.txt", "w") as f:
        for course, count in course_count.items():
            f.write(f"{course} = {count}\n")

with DAG(
    dag_id="exercise14_course_enrollment_report",
    start_date=datetime(2025,1,1),
    schedule=None,
    catchup=False
) as dag:

    t1 = PythonOperator(task_id="create_enrollment_file", python_callable=create_enrollment_file)
    t2 = PythonOperator(task_id="count_students", python_callable=count_students)
    t3 = PythonOperator(task_id="generate_course_report", python_callable=generate_course_report)

    t1 >> t2 >> t3