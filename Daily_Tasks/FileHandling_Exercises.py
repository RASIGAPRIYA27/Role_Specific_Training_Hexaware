# 1 Read and display entire file
file = open("employees.txt", "r")
data = file.read()
print(data)
file.close()


# 2 Display file line by line

file = open("employees.txt", "r")

for line in file:
    print(line.strip())

file.close()


# 3 Count total employees
file = open("employees.txt", "r")
count = len(file.readlines())
print("Total Employees =", count)
file.close()


# 4 Display only employee names

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")
    print(data[1])

file.close()


# 5 Display employees from Hyderabad

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    if data[4] == "Hyderabad":
        print(data)

file.close()


# 6 Display employees from Bangalore

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    if data[4] == "Bangalore":
        print(data)

file.close()


# 7 Display employees whose salary is greater than 80000

file = open("employees.txt", "r")
for line in file:
    data = line.strip().split(",")

    if int(data[3]) > 80000:
        print(data)

file.close()


# 8 Find highest salary

file = open("employees.txt", "r")
highest = 0
for line in file:
    data = line.strip().split(",")

    if int(data[3]) > highest:
        highest = int(data[3])

print("Highest Salary =", highest)

file.close()


# 9 Find lowest salary

file = open("employees.txt", "r")

salaries = []

for line in file:
    data = line.strip().split(",")
    salaries.append(int(data[3]))

print("Lowest Salary =", min(salaries))

file.close()


# 10 Find average salary

file = open("employees.txt", "r")
total = 0
count = 0
for line in file:
    data = line.strip().split(",")

    total += int(data[3])
    count += 1

print("Average Salary =", total / count)

file.close()


# 11 Calculate total salary payout

file = open("employees.txt", "r")

total_salary = 0

for line in file:
    data = line.strip().split(",")

    total_salary += int(data[3])

print("Total Salary =", total_salary)

file.close()


# 12 Count employees in AI Engineering

file = open("employees.txt", "r")

count = 0

for line in file:
    data = line.strip().split(",")

    if data[2] == "AI Engineering":
        count += 1

print("AI Engineering =", count)

file.close()


# 13 Count employees in Data Engineering

file = open("employees.txt", "r")
count = 0
for line in file:
    data = line.strip().split(",")

    if data[2] == "Data Engineering":
        count += 1

print("Data Engineering =", count)

file.close()


# 14 Display employees whose department is AI Engineering

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    if data[2] == "AI Engineering":
        print(data)

file.close()


# 15 Create high_salary_employees.txt

file = open("employees.txt", "r")
output = open("high_salary_employees.txt", "w")

for line in file:
    data = line.strip().split(",")

    if int(data[3]) > 80000:
        output.write(line)

file.close()
output.close()


# 16 Create hyderabad_employees.txt

file = open("employees.txt", "r")
output = open("hyderabad_employees.txt", "w")

for line in file:
    data = line.strip().split(",")

    if data[4] == "Hyderabad":
        output.write(line)

file.close()
output.close()


# 17 Count unique cities

file = open("employees.txt", "r")
cities = set()
for line in file:
    data = line.strip().split(",")

    cities.add(data[4])

for city in cities:
    print(city)

print("Total Cities =", len(cities))

file.close()


# 18 Count employees by department
file = open("employees.txt", "r")
departments = {}
for line in file:
    data = line.strip().split(",")

    dept = data[2]
    if dept in departments:
        departments[dept] += 1
    else:
        departments[dept] = 1

for dept, count in departments.items():
    print(dept, "=", count)

file.close()


# 19 Find employee with highest salary
file = open("employees.txt", "r")
highest_salary = 0
employee_name = ""

for line in file:
    data = line.strip().split(",")

    salary = int(data[3])
    if salary > highest_salary:
        highest_salary = salary
        employee_name = data[1]

print(employee_name)
print(highest_salary)
file.close()


# 20 Generate employee_report.txt

file = open("employees.txt", "r")
salaries = []

for line in file:
    data = line.strip().split(",")

    salaries.append(int(data[3]))
report = open("employee_report.txt", "w")

report.write("Total Employees = " + str(len(salaries)) + "\n")
report.write("Highest Salary = " + str(max(salaries)) + "\n")
report.write("Lowest Salary = " + str(min(salaries)) + "\n")
report.write("Average Salary = " + str(sum(salaries) / len(salaries)) + "\n")
report.write("Total Salary = " + str(sum(salaries)) + "\n")

report.close()
file.close()