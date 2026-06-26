import pandas as pd
import numpy as np


# 1
# Create sample dataset and save to CSV
sample_data = [
    [101, 1, "Rice", "2026-06-01", "2026-06-05", 50, 40, 32.5, "Delivered", "High", "On time"],
    [102, 2, "Wheat", "2026-06-02", "2026-06-08", 30, 18, 28.0, "Delivered", "Medium", "Late due to transport"],
    [103, 3, "Sugar", "2026-06-03", None, 20, 25, 41.0, "Pending", "Low", None],
    [104, 1, "Salt", "2026-06-04", "2026-06-06", 10, 12, 15.0, "Delivered", "High", "Fast delivery"],
    [105, 4, "Oil", "2026-06-05", "2026-06-10", 15, 8, 120.0, "Delivered", "Medium", "Small delay"],
    [106, 5, "Tea", "2026-06-06", "2026-06-09", 40, 35, 220.0, "Delivered", "Low", "Good"],
    [107, 2, "Coffee", "2026-06-07", "2026-06-12", 25, 20, 310.0, "Delivered", "High", "Delay"],
    [108, 3, "Milk Powder", "2026-06-08", "2026-06-13", 18, 10, 450.0, "Delivered", "Medium", ""],
    [109, 4, "Biscuit", "2026-06-09", "2026-06-11", 60, 55, 20.0, "Delivered", "Low", "Good stock"],
    [110, 5, "Soap", "2026-06-10", None, 35, 30, 25.0, "Pending", "High", "Waiting for shipment"],
]

columns = ["order_id", "supplier_id", "product_name", "order_date", "delivery_date",
           "ordered_qty", "stock_on_hand", "unit_price", "status", "priority", "notes"]

df_sample = pd.DataFrame(sample_data, columns=columns)

df_sample.to_csv("sample_supply_chain_data.csv", index=False)

print("Sample dataset created: sample_supply_chain_data.csv")

print(df_sample.head())

# 2
# Load the dataset from CSV
df = pd.read_csv("sample_supply_chain_data.csv")

# 3
# Clean data
df = df.drop_duplicates()

df = df.dropna(subset=["order_id", "supplier_id", "order_date"])

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

df["delivery_date"] = pd.to_datetime(df["delivery_date"], errors="coerce")

df['priority'] = df['priority'].str.title()

# 4
# Fill missing values
df["notes"] = df["notes"].fillna("No notes")

df["delivery_date"] = df["delivery_date"].fillna(pd.Timestamp("2026-06-26"))

# 5
# Numpy calculations
df["delay_days"] = (df["delivery_date"] - df["order_date"]).dt.days

df["stock_gap"] = np.where(df["stock_on_hand"] < df["ordered_qty"],
                           df["ordered_qty"] - df["stock_on_hand"], 0)

df["is_delayed"] = np.where(df["delay_days"] > 3, 1, 0)

avg_delay = np.mean(df['delay_days'])

total_stock_gap = np.sum(df['stock_gap'])

total_inventory_value = np.sum(df['total_value'])

# 6
# Display cleaned and processed data
print(df[["order_id", "supplier_id", "product_name", "order_date", "delivery_date",
          "delay_days", "stock_gap", "is_delayed"]])

# 7
# Basic summary
print("Total Orders:", len(df))
print("Average Delay Days:", np.mean(df["delay_days"]))
print("Total Stock Gap:", np.sum(df["stock_gap"]))


# 8
df.to_csv('processed_supply_chain_data.csv', index=False)
print('\nProcessed file saved as: processed_supply_chain_data.csv')