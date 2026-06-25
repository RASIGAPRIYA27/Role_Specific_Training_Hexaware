from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_department_file():
    with open("/tmp/departments.txt", "w") as f:
        f.write("""IT,45000
HR,35000
Finance,50000
IT,55000
Finance,40000
HR,30000""")

def calculate_department_salary(ti):
    dept_salary = {}

    with open("/tmp/departments.txt") as f:
        for line in f:
            dept, salary = line.strip().split(",")
            dept_salary[dept] = dept_salary.get(dept, 0) + int(salary)

    ti.xcom_push(key="dept_salary", value=dept_salary)

def generate_department_report(ti):
    dept_salary = ti.xcom_pull(
        task_ids="calculate_department_salary",
        key="dept_salary"
    )

    with open("/tmp/department_report.txt", "w") as f:
        for dept, total in dept_salary.items():
            f.write(f"{dept} = {total}\n")

with DAG(
    dag_id="exercise7_department_salary_report",
    start_date=datetime(2025,1,1),
    schedule=None,
    catchup=False
) as dag:

    t1 = PythonOperator(task_id="create_department_file", python_callable=create_department_file)
    t2 = PythonOperator(task_id="calculate_department_salary", python_callable=calculate_department_salary)
    t3 = PythonOperator(task_id="generate_department_report", python_callable=generate_department_report)

    t1 >> t2 >> t3