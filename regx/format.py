import re

name = input("What is your name? ")

if matches := re.search("^(.+), *?(.+)$", name):
    f_name, l_name = matches.groups()
    name = f"{f_name} {l_name}"
print(name)