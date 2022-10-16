with open("student.csv") as file:
    for line in file:
        name,hall,year = line.rstrip().split(",")
        print(f"{name} is in  {hall} born in {year}")