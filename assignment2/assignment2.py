import csv
import os
import sys
import traceback
from datetime import datetime


#Task  2
def read_employees():
    result = {'fields': [], 'rows': []}
    try:
        with open('../csv/employees.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    result['fields'] = row
                else:
                    result['rows'].append(row)
    except Exception as e:
        print(f"Error reading employees.csv: {e}")
        raise
    return result

employees = read_employees()


# Task3
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")
print(employee_id_column)

# Task 4
def first_name(row_index):
    first_name_idx = column_index("first_name")
    return employees["rows"][row_index][first_name_idx]

# Task5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    return list(filter(employee_match, employees["rows"]))

# Task 6
def employee_find_2(employee_id):
    return list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))

# Task 7
def sort_by_last_name():
    last_name_idx = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_idx])
    return employees["rows"]


# Task8
def employee_dict(row):
    return {
        field: row[idx]
        for idx, field in enumerate(employees["fields"])
        if field != "employee_id"
    }

# Task 9
def all_employees_dict():
    return {
        row[employee_id_column]: employee_dict(row)
        for row in employees["rows"]
    }

# Task 10
def get_this_value():
    return os.getenv('THISVALUE')

# Task 11
import custom_module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

print(custom_module.secret)

# Task 12
def read_minutes():
    def read_file(filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                rows = list(reader)
                return {
                    "fields": rows[0],
                    "rows": [tuple(row) for row in rows[1:]]
                }
        except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(f'File : {trace[0]}, Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            if str(e):
                print(f"Exception message: {str(e)}")
            print(f"Stack trace: {stack_trace}")
            sys.exit(1)
    
    return (
        read_file('../csv/minutes1.csv'),
        read_file('../csv/minutes2.csv')
    )

minutes1, minutes2 = read_minutes()

# Task13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)

minutes_set = create_minutes_set()

# Task 14
def create_minutes_list():
    minutes_list = list(minutes_set)
    return list(map(
        lambda t: (t[0], datetime.strptime(t[1], "%B %d, %Y")),
        minutes_list
    ))

minutes_list = create_minutes_list()

# Task 15
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    converted_list = list(map(
        lambda t: (t[0], t[1].strftime("%B %d, %Y")),
        sorted_list
    ))
    
    with open('minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)
    
    return converted_list

# Additional calls for demonstration
if __name__ == "__main__":
    print("Employees data:", employees)
    print("Employee ID column:", employee_id_column)
    print("First employee's first name:", first_name(0))
    print("Employee with ID 101:", employee_find(101))
    sort_by_last_name()
    print("Employee dict:", employee_dict(employees["rows"][0]))
    print("All employees dict:", all_employees_dict())
    print("THISVALUE:", get_this_value())
    
    # Demonstrate custom module
    print("Original secret:", custom_module.secret)
    custom_module.set_secret("new_secret")
    print("Updated secret:", custom_module.secret)
    
    write_sorted_list()