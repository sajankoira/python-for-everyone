"""
TOPIC: JSON & CSV - Real world data handling
"""

import json
import csv
import os

# --- JSON ---
students = [
    {"name": "Amit", "roll": 101, "marks": 90, "city": "Belagavi"},
    {"name": "Priya", "roll": 102, "marks": 95, "city": "Pune"},
    {"name": "Rahul", "roll": 103, "marks": 85, "city": "Mumbai"}
]

# Write
with open("students.json", "w") as f:
    json.dump(students, f, indent=2)

# Read + find topper
with open("students.json", "r") as f:
    data = json.load(f)
    topper = max(data, key=lambda x: x["marks"])
    print(f"Topper: {topper['name']} with {topper['marks']}")

# Pretty print JSON
print(json.dumps(topper, indent=2))

# --- CSV ---
# Write
with open("employees.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name","dept","salary"])
    writer.writeheader()
    writer.writerows([
        {"name": "Sajan", "dept": "IT", "salary": 60000},
        {"name": "Amit", "dept": "HR", "salary": 50000},
    ])

# Read
with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    total = 0
    for row in reader:
        print(row)
        total += int(row["salary"])
    print(f"Total salary: {total}")

# --- Cleanup ---
for file in ["students.json", "employees.csv", "temp_demo.txt", "my_custom_module.py", "todo.json", "demo.txt", "data.json", "students.csv"]:
    if os.path.exists(file):
        os.remove(file)

print("\nFiles cleaned")
