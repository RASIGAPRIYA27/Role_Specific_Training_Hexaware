import pandas as pd
import numpy as np

# 1
# Create sample dataset and save to CSV
sample_data = [
    [1001, "C101", "2026-06-01 10:30:00", "2026-06-05 15:00:00", "Delivered", "Late delivery", 1250.50, "Card"],
    [1002, "C102", "2026-06-02 11:00:00", "2026-06-03 17:00:00", "Delivered", "Address issue", 840.00, "UPI"],
    [1003, "C103", "2026-06-03 09:15:00", None, "Pending", None, 560.75, "Cash"],
    [1004, "C101", "2026-06-04 14:20:00", "2026-06-10 18:30:00", "Delivered", "Weather delay", 1999.00, "Card"],
    [1005, "C104", "2026-06-05 08:45:00", "2026-06-07 13:10:00", "Delivered", "On time", 430.20, "Net Banking"],
    [1006, "C105", "2026-06-06 16:00:00", "2026-06-12 19:45:00", "Delivered", "Late delivery", 780.00, "UPI"],
    [1007, "C102", "2026-06-07 12:10:00", "2026-06-09 10:30:00", "Delivered", "Damaged package", 1500.00, "Card"],
    [1008, "C106", "2026-06-08 17:25:00", "2026-06-15 20:00:00", "Delivered", "Delivery partner delay", 920.60, "Cash"],
    [1009, "C107", "2026-06-09 13:40:00", "2026-06-10 16:20:00", "Delivered", "On time", 300.00, "UPI"],
    [1010, "C105", "2026-06-10 09:50:00", None, "Pending", "Awaiting shipment", 670.90, "Card"]
]

columns = ["order_id", "customer_id", "order_date", "delivery_date",
           "delivery_status", "delivery_issue", "order_amount", "payment_mode"]

df_sample = pd.DataFrame(sample_data, columns=columns)

df_sample.to_csv("sample_customer_orders.csv", index=False)

print("Sample dataset created: sample_customer_orders.csv")

print(df_sample.head())

# 2
# Load the dataset from CSV
df = pd.read_csv("sample_customer_orders.csv")

# 3
# Clean data
df = df.drop_duplicates()

df = df.dropna(subset=["order_id", "customer_id", "order_date"])

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

df["delivery_date"] = pd.to_datetime(df["delivery_date"], errors="coerce")

# 4
# Fill missing values
df["delivery_issue"] = df["delivery_issue"].fillna("No issue reported")

df["delivery_date"] = df["delivery_date"].fillna(pd.Timestamp("2026-06-26"))

df["delivery_status"] = df["delivery_status"].fillna("Pending")

# 5
# Numpy calculations
df["delay_days"] = (df["delivery_date"] - df["order_date"]).dt.days

df["is_delayed"] = np.where(df["delay_days"] > 3, 1, 0)

# 6
# Display cleaned and processed data
print(df[["order_id", "customer_id", "order_date", "delivery_date",
          "delivery_status", "delivery_issue", "delay_days", "is_delayed"]])

# 7
# Basic summary
print("Total Orders:", len(df))
print("Average Delay Days:", np.mean(df["delay_days"]))
print("Total Delayed Orders:", np.sum(df["is_delayed"]))

# 8
# Delay summary by customer
print("Delay Summary by Customer:")
print(df.groupby("customer_id")["is_delayed"].sum().sort_values(ascending=False))

# 9
# Top delayed customers
print("Top Delayed Customers:")
print(df.groupby("customer_id")["delay_days"].sum().sort_values(ascending=False).head())

# 10
# Most common delivery issues
print("Most Common Delivery Issues:")
print(df["delivery_issue"].value_counts())

# 11
# Save cleaned and processed dataset
df.to_csv("processed_customer_orders.csv", index=False)
print("Processed dataset saved: processed_customer_orders.csv")