with open("student.csv") as file:
    for line in file:
        name,hall,year = line.rstrip().split(",")
        print(f"{name} is in  {hall} born in {year}")
story = [
    "This is Cs50P",
    "This is Cs50P",
    "This is Cs50P",
    "This is Cs50P",
    "This is Cs50P",
    "This is Cs50P",
    "This is Cs50P",
    "This is Cs50P",
    "This is Cs50P",
    "This is Cs50P",
    "This is Cs50P",
    "This is Cs50P",
    "This is Cs50P",
    "This is Cs50P",
    "This is Cs50P",
]


with open("marcus.txt",'a') as file:
    for line in story:
        file.write(f"{line}\n")

with open("marcus.txt", 'r') as file:
    for line in file.readlines():
        print(f"{line.strip()}")

