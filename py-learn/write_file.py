import json
import csv

txt_data = "I like donuts."

# employees = ["Eugene", "Alice", "Bob", "Charlie"]

# employee_dict = {"name": "Eugene", "age": 30, "position": "Software Engineer"}

employees = [
    ["Name", "Age", "Position"],
    ["Eugene", 30, "Software Engineer"],
    ["Alice", 25, "Data Scientist"],
    ["Bob", 35, "Product Manager"],
]

# file_path = "py-learn/donuts.txt"
# file_path = "py-learn/output.json"
file_path = "py-learn/employees.csv"

try:
    with open(file_path, "w", newline="") as file:
        # for employee in employees:
        #     file.write(f"{employee} likes donuts.\n")
        # json.dump(employee_dict, file, indent=4)
        writer = csv.writer(file)
        writer.writerows(employees)
        print(f"Data written to '{file_path}'")
except FileExistsError:
    print(f"Error: The file '{file_path}' already exists.")
