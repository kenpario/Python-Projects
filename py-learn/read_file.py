import json
import csv

file_path = "py-learn/employees.csv"

try:
    with open(file_path, "r") as file:
        # content = file.read()
        # content = json.load(file)
        content = csv.reader(file)
        for line in content:
            print(line[2])
        # print(content["position"])
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except PermissionError:
    print(f"Error: You do not have permission to read the file '{file_path}'.")
