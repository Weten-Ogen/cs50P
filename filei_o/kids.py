import csv


name = input("What's the name? ")
house = input("What's the house? ")
year = input("What's the year? ")




with open("student.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house", "year"])
    writer.writerow({"name":name, "house":house, "year":year})
