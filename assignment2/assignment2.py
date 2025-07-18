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