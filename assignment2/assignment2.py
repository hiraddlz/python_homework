import csv

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