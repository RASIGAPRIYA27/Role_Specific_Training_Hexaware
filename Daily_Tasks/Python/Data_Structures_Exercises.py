salaries = [45000, 55000, 65000, 75000, 85000]

# 1 Display all salaries
print(salaries)

# 2 Find maximum and minimum salary
print("Maximum Salary:", max(salaries))
print("Minimum Salary:", min(salaries))

# 3 Find total salary
print("Total Salary:", sum(salaries))

# 4 Find average salary
print("Average Salary:", sum(salaries) / len(salaries))

# 5 Add new salaries
salaries.append(95000)
salaries.append(105000)
print(salaries)

# 6 Remove salary 55000
salaries.remove(55000)
print(salaries)

# 7 Sort salaries in ascending order
print(sorted(salaries))

# 8 Sort salaries in descending order
print(sorted(salaries, reverse=True))

# 9 Find second highest salary
print(sorted(salaries, reverse=True)[1])

# 10 Display salaries greater than 70000
for salary in salaries:
    if salary > 70000:
        print(salary)

employee = (
    101,
    "Rahul Sharma",
    "Data Engineering",
    75000
)

# 11 Display employee tuple
print(employee)

# 12 Display employee name
print(employee[1])

# 13 Display employee department
print(employee[2])

# 14 Unpack tuple values
emp_id, name, department, salary = employee

print(emp_id)
print(name)
print(department)
print(salary)

# 15 Display tuple length, first and last element
print("Length:", len(employee))
print("First Element:", employee[0])
print("Last Element:", employee[-1])

batch_a = {"Rahul", "Priya", "Amit", "Sneha", "Farhan"}
batch_b = {"Priya", "Sneha", "Neha", "Arjun", "Farhan"}

# 16 Find common students
print(batch_a.intersection(batch_b))

# 17 Find students only in batch A
print(batch_a - batch_b)

# 18 Find students only in batch B
print(batch_b - batch_a)

# 19 Find union of both batches
print(batch_a.union(batch_b))

# 20 Find symmetric difference
print(batch_a.symmetric_difference(batch_b))

employee_info = {
    "employee_id": 101,
    "name": "Rahul Sharma",
    "department": "Data Engineering",
    "salary": 75000,
    "city": "Hyderabad"
}

# 21 Display employee name
print(employee_info["name"])

# 22 Display department and city
print(employee_info["department"])
print(employee_info["city"])

# 23 Add experience key
employee_info["experience"] = 5
print(employee_info)

# 24 Update salary
employee_info["salary"] = 85000
print(employee_info)

# 25 Remove city key
employee_info.pop("city")
print(employee_info)

# 26 Display all keys
print(employee_info.keys())

# 27 Display all values
print(employee_info.values())

# 28 Display all key-value pairs
print(employee_info.items())

employees = [
    {"id": 101, "name": "Rahul", "department": "IT", "salary": 50000},
    {"id": 102, "name": "Priya", "department": "HR", "salary": 70000},
    {"id": 103, "name": "Amit", "department": "IT", "salary": 60000},
    {"id": 104, "name": "Sneha", "department": "Finance", "salary": 80000},
    {"id": 105, "name": "Farhan", "department": "IT", "salary": 90000}
]

# 29 Display all employee names
for emp in employees:
    print(emp["name"])

# 30 Display IT employees
for emp in employees:
    if emp["department"] == "IT":
        print(emp)

# 31 Find employee with highest salary
print(max(employees, key=lambda x: x["salary"]))

# 32 Find employee with lowest salary
print(min(employees, key=lambda x: x["salary"]))

# 33 Find average salary
avg_salary = sum(emp["salary"] for emp in employees) / len(employees)
print(avg_salary)

# 34 Find total salary
total_salary = sum(emp["salary"] for emp in employees)
print(total_salary)

# 35 Display employees with salary greater than 70000
for emp in employees:
    if emp["salary"] > 70000:
        print(emp)

# 36 Count IT employees
count = 0

for emp in employees:
    if emp["department"] == "IT":
        count += 1

print(count)

# 37 Sort employees by salary in descending order
sorted_employees = sorted(
    employees,
    key=lambda x: x["salary"],
    reverse=True
)

for emp in sorted_employees:
    print(emp)

# 38 Display second highest paid employee
sorted_employees = sorted(
    employees,
    key=lambda x: x["salary"],
    reverse=True
)

print(sorted_employees[1])

# 39 Display unique departments
departments = set()

for emp in employees:
    departments.add(emp["department"])

print(departments)
