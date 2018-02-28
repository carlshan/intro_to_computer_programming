class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print("Hi I'm " + self.name + " and I'm in " + str(self.grade) + "th grade.")
