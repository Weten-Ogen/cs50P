# A list of names
names =[
    "Marcus",
    "Gideon",
    "Hermione",
    "Ron",
    "Harry",
    "Ginny",
]

# Adds a new person to names
def addto(names,name):
    if name not in names:
        names = names.append(name)
    else:
        print("You are in the group")

# Prompt for name
while True:
    name = input("Name please: ")
    addto(names, name)

# Prints all names
for name in names:
    print(name)