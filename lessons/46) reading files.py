import json
import csv

# file_path = "/Users/macbookair/Desktop/output.txt"
# file_path = "/Users/macbookair/Desktop/output.json"
file_path = "/Users/macbookair/Desktop/output.csv"

try:
    with open(file_path, "r") as file:
        # content = file.read()
        # content = json.load(file)
        content = csv.reader(file)
        for line in content:
            print(line[0])
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")