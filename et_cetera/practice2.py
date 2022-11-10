# A list of names 
list_of_names =[
    "Marcus", "Agnes", "Alice", "Richmond","Nicholas","Harry","Hermione","Ron", "LongBottom", "Luna","Cho",
]
# A set of names
names =set(list_of_names)

# Adds a person to the set
def insertinto(names, name):
    if name not in names:
        names = names.add(name)

# Request of a name
name = input("Enter a name : ")

insertinto(names,name)

# Loop over the new names
for name in names:
    print(name)
