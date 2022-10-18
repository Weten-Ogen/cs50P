import csv

students = []
with open("student.csv") as file:
    reader = csv.reader(file)
    for name,house,year in reader:
         students.append({"name":name, "house":house, "year":year})

for student in students:
     print(f"{student['name']} is in {student['house']} was born on {student['year']}") 
    