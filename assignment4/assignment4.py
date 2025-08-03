import pandas as pd

### task 1
#Step 1
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(data)
print("Task 1 - Initial DataFrame:")
print(task1_data_frame)

# Step 2
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("\nTask 1 - DataFrame with Salary:")
print(task1_with_salary)

# Step3
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print("\nTask 1 - Older Employees:")
print(task1_older)

# step4
task1_older.to_csv('employees.csv', index=False)
print("\nCSV file saved: employees.csv")


## task 2
# step 1
task2_employees = pd.read_csv('employees.csv')
print("\nTask 2 - Employees from CSV:")
print(task2_employees)

# Step 2
json_data = """
[
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]
"""
with open('additional_employees.json', 'w') as f:
    f.write(json_data)
    
json_employees = pd.read_json('additional_employees.json')
print("\nTask 2 - JSON Employees:")
print(json_employees)

# Step 3
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nTask2 -Combined Employees:")
print(more_employees)



# Task3
# Step 1
first_three = more_employees.head(3)
print("\nTask 3 - First Three Employees:")
print(first_three)

# step 2
last_two = more_employees.tail(2)
print("\nTask 3- Last Two Employees:")
print(last_two)

# Step 3 
employee_shape = more_employees.shape
print(f"\nTask 3 - DataFrame Shape: {employee_shape}")

# Step 4
print("\nTask3 - DataFrame Info:")
print(more_employees.info())