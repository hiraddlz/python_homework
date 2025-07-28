import csv
import os

path = os.path.abspath('./csv/employees.csv')

# Read employees.csv
with open(path, 'r') as f:
    reader = csv.reader(f)
    employees = list(reader)[1:]  # Skip header

# Create list of full names
full_names = [f"{row[1]} {row[2]}" for row in employees]
print("Full Names:", full_names)

# Filter names containing 'e'
names_with_e = [name for name in full_names if 'e' in name.lower()]
print("\nNames containing 'e':", names_with_e)