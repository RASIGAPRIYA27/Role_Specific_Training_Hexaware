import csv
import numpy as np
import pandas as pd

# 1 read orders.csv
with open ("orders.csv","r") as file:
    reader=file.read()
    print(reader)

#2 display all records
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#3 count total orders
with open ("orders.csv","r") as file:
    reader = file.readlines()
print("Total Orders : ",len(reader)-1)

#4 total revenue
with open ("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    rev=0
    for row in reader:
        rev+=int(row[5]) * int(row[6])
print("Total Revenues : ",rev)

#5 highest order
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    high = 0
    for row in reader:
        order_value = int(row[5]) * int(row[6])
        if order_value > high:
            high = order_value
print("Highest Order Value :", high)

#6 lowest order
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    low = high
    for row in reader:
        order_value = int(row[5]) * int(row[6])
        if order_value < low:
            low = order_value
print("Lowest Order Value :", low)

#7 average order
with open ("orders.csv","r") as file:
    reader = file.readlines()
    avg=rev/(len(reader)-1)
print("Average order value : ",avg)

#8 unique customers
with open ("orders.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    data=set()
    for row in reader:
        data.add(row[1])
    print("Unique Customers :")
    for d in data:
        print(d)

#9 count unique customer
print("Unique customer Count :",len(data))

#10 Customer with highest order value
with open ("orders.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if int(row[6]) * int(row[5])==high:
            print("Customer with Highest Purchase :",row[1])
            break

#11 count orders by product
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    product_count = {}
    for row in reader:
        product = row[3]
        if product in product_count:
            product_count[product] += 1
        else:
            product_count[product] = 1
print("Orders by Product :", product_count)

# 12 calculate revenue by product
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    product_rev = {}
    for row in reader:
        product = row[3]
        amount = int(row[5]) * int(row[6])
        if product in product_rev:
            product_rev[product] += amount
        else:
            product_rev[product] = amount
print("Revenue by Product :", product_rev)

#13 most sold product
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    pro_qty = {}
    for row in reader:
        product = row[3]
        qty = int(row[5])
        if product in pro_qty:
            pro_qty[product] += qty
        else:
            pro_qty[product] = qty
top_product = max(pro_qty, key=pro_qty.get)
print("Most Sold Product :", top_product, pro_qty[top_product])

#14 least sold
least_product = min(pro_qty, key=pro_qty.get)
print("Least Sold Product :", least_product, pro_qty[least_product])

#15 Revenue by category
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    category_revenue = {}
    for row in reader:
        category = row[4]
        amt = int(row[5]) * int(row[6])
        if category in category_revenue:
            category_revenue[category] += amt
        else:
            category_revenue[category] = amt
print("Revenue by Category :", category_revenue)

#16 count orders by city
with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    cnt={}
    for row in reader:
        city=row[2]
        if city in cnt:
            cnt[city] += 1
        else:
            cnt[city] = 1
    print("Count by City :",cnt)

#17 Revenue by city
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    city_revenue = {}
    for row in reader:
        city = row[2]
        amt = int(row[5]) * int(row[6])
        if city in city_revenue:
            city_revenue[city] += amt
        else:
            city_revenue[city] = amt
print("Revenue by City :", city_revenue)

#18 City with highest revenue
top_city = max(city_revenue, key=city_revenue.get)
print("Top Revenue Generating City :", top_city)

#19 list operations
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    prod=[]
    for row in reader:
        prod.append(row[3])
prod.sort()
print(prod)

#20 unique cities
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    city=set()
    for row in reader:
        city.add(row[2])
print(city)

#21 city dictionary
print("City Revenue Dictionary :", city_revenue)

#22 product dictionary
print("Product Quantity Dictionary :", pro_qty)

#23 calculate revenue function
def calculate_total_revenue():
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        total = 0
        for row in reader:
            total += int(row[5]) * int(row[6])
    return total

print("Function Total Revenue :", calculate_total_revenue())

#24 top product function
def find_top_product():
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        p = {}
        for row in reader:
            product = row[3]
            qty = int(row[5])
            if product in p:
                p[product] += qty
            else:
                p[product] = qty
    top = max(p, key=p.get)
    return top, p[top]

print("Function Top Product :", find_top_product())

# 25 function find_top_city()
def find_top_city():
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        c = {}
        for row in reader:
            city = row[2]
            amount = int(row[5]) * int(row[6])
            if city in c:
                c[city] += amount
            else:
                c[city] = amount
    top = max(c, key=c.get)
    return top, c[top]

print("Function Top City :", find_top_city())

# 26 function find_average_order_value()
def find_average_order_value():
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        total = 0
        count = 0
        for row in reader:
            total += int(row[5]) * int(row[6])
            count += 1
    return total / count

print("Function Average Order Value :", find_average_order_value())

# 27 handle missing CSV file
try:
    with open("orders.csv", "r") as file:
        print("File opened successfully")
except FileNotFoundError:
    print("orders.csv file is missing")

# 28 handle invalid quantity values
try:
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            qty = int(row[5])
except ValueError:
    print("Invalid quantity value found")


# 29 handle invalid price values
try:
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            price = int(row[6])
except ValueError:
    print("Invalid price value found")

# 30 NumPy array and calculations
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    values = []
    for row in reader:
        values.append(int(row[5]) * int(row[6]))

arr = np.array(values)
print("NumPy Total Revenue :", np.sum(arr))
print("NumPy Average Revenue :", np.mean(arr))
print("NumPy Maximum Revenue :", np.max(arr))
print("NumPy Minimum Revenue :", np.min(arr))
print("NumPy Standard Deviation :", np.std(arr))


# 31 read CSV using pandas
df = pd.read_csv("orders.csv")
print(df)

# 32 create revenue column
df["Revenue"] = df["quantity"] * df["price"]
print(df)

# 33 display top 5 highest value orders
print(df.sort_values("Revenue", ascending=False).head(5))

# 34 group by city and calculate revenue
print(df.groupby("city")["Revenue"].sum())

# 35 group by product and calculate revenue
print(df.groupby("product")["Revenue"].sum())

# 36 display top selling products
print(df.groupby("product")["quantity"].sum().sort_values(ascending=False))

# 37 display city-wise order count
print(df["city"].value_counts())

# report generation
with open("sales_summary_report.txt", "w") as file:
    file.write("Total Orders : " + str(len(df)) + "\n")
    file.write("Total Revenue : " + str(df["Revenue"].sum()) + "\n")
    file.write("Average Order Value : " + str(df["Revenue"].mean()) + "\n")
    file.write("Highest Order Value : " + str(df["Revenue"].max()) + "\n")
    file.write("Lowest Order Value : " + str(df["Revenue"].min()) + "\n\n")

    file.write("Revenue By City\n")
    file.write(str(df.groupby("city")["Revenue"].sum()) + "\n\n")

    file.write("Revenue By Category\n")
    file.write(str(df.groupby("category")["Revenue"].sum()) + "\n\n")

    file.write("Top Selling Product\n")
    file.write(str(df.groupby("product")["quantity"].sum().sort_values(ascending=False).head(1)) + "\n\n")

    file.write("Top Revenue Generating City\n")
    file.write(str(df.groupby("city")["Revenue"].sum().sort_values(ascending=False).head(1)) + "\n")

print("sales_summary_report.txt created")

# 38 high_value_orders.csv
high_value = df[df["Revenue"] > 50000]
high_value.to_csv("high_value_orders.csv", index=False)
print("high_value_orders.csv created")

# 39 electronics_orders.csv
electronics = df[df["category"] == "Electronics"]
electronics.to_csv("electronics_orders.csv", index=False)
print("electronics_orders.csv created")

# 40 menu driven application
while True:
    print("\n1. View Orders")
    print("2. Revenue Analysis")
    print("3. Product Analysis")
    print("4. City Analysis")
    print("5. Export Reports")
    print("6. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        print(df)

    elif choice == "2":
        print("Total Revenue :", df["Revenue"].sum())
        print("Average Order Value :", df["Revenue"].mean())
        print("Highest Order Value :", df["Revenue"].max())
        print("Lowest Order Value :", df["Revenue"].min())

    elif choice == "3":
        print(df.groupby("product")["quantity"].sum().sort_values(ascending=False))
        print(df.groupby("product")["Revenue"].sum())

    elif choice == "4":
        print(df.groupby("city")["Revenue"].sum())
        print(df["city"].value_counts())

    elif choice == "5":
        high_value.to_csv("high_value_orders.csv", index=False)
        electronics.to_csv("electronics_orders.csv", index=False)
        print("Reports exported successfully")

    elif choice == "6":
        print("Exited")
        break

    else:
        print("Invalid Choice")
