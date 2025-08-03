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
