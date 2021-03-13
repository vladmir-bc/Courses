import csv

students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]

with open("example1.csv", "a", newline='') as f:
    writer = csv.writer(f)
    for student in students:
        writer.writerow(student)