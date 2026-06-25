from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_transactions():
    with open("/tmp/transactions.txt", "w") as f:
        f.write("""Deposit,10000
Withdraw,2500
Deposit,4000
Withdraw,1500
Deposit,2000""")

def calculate_balance(ti):
    deposits = 0
    withdrawals = 0

    with open("/tmp/transactions.txt") as f:
        for line in f:
            txn, amount = line.strip().split(",")

            if txn == "Deposit":
                deposits += int(amount)
            else:
                withdrawals += int(amount)

    balance = deposits - withdrawals

    ti.xcom_push(key="deposits", value=deposits)
    ti.xcom_push(key="withdrawals", value=withdrawals)
    ti.xcom_push(key="balance", value=balance)

def generate_account_report(ti):
    deposits = ti.xcom_pull(task_ids="calculate_balance", key="deposits")
    withdrawals = ti.xcom_pull(task_ids="calculate_balance", key="withdrawals")
    balance = ti.xcom_pull(task_ids="calculate_balance", key="balance")

    with open("/tmp/account_report.txt", "w") as f:
        f.write(
            f"Total Deposit = {deposits}\n"
            f"Total Withdrawal = {withdrawals}\n"
            f"Final Balance = {balance}"
        )

with DAG(
    dag_id="exercise12_bank_transaction_summary",
    start_date=datetime(2025,1,1),
    schedule=None,
    catchup=False
) as dag:

    t1 = PythonOperator(task_id="create_transactions", python_callable=create_transactions)
    t2 = PythonOperator(task_id="calculate_balance", python_callable=calculate_balance)
    t3 = PythonOperator(task_id="generate_account_report", python_callable=generate_account_report)

    t1 >> t2 >> t3