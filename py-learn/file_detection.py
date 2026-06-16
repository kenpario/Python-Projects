import os

file_path = "py-learn/text/file_detection.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists.")
    if os.path.isfile(file_path):
        print(f"The location '{file_path}' is a file.")
    elif os.path.isdir(file_path):
        print(f"The location '{file_path}' is a directory.")
else:
    print(f"The location '{file_path}' does not exist.")
