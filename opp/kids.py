class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

    # Gets the name ins. variable
    @property
    def name(self):
        return self._name
    
    # Sets the name ins. variable
    @name.setter
    def name(self, name):
        if name not in ["Harry", "Ron", "Griny", "Hermione"]:
            raise ValueError
        self._name = name
            


def main():
    # student has a name and house
    student = get_student()
    # Display the name and house of student
    print(f"{student.name} is in {student.house}")

def get_student():
    # Request for user's name
    name = input("Name: ")
    # Request for user's input
    house = input("House: ")
    # Returns name and the house
    return Student(name,house)







if __name__ == "__main__":
    main()