students = []

# Opens the student.csv file
with open("student.csv") as file:
    # read through line by line
    for line in file.readlines():
        # unpack each value in variable
        name, house, year = line.rstrip().split(',')
        # a dict blueprint for each student
        student = {
            "name" : name,
            "house": house,
            }
        students.append(student)
def get_name(student):
    return student['house']

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")


