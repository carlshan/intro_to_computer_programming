class Teacher:
    def __init__(self, subject_taught, ease):
        self.subject_taught = subject_taught
        self.ease = ease

    def give_grade(self, student, grade_given):
        if self.subject_taught == 'CS':
            student.grades.append(100)
        else:
            student.grades.append(grade_given)


class NuevaTeacher(Teacher):
    pass


class Student:
    def __init__(self, grades):
        self.grades = grades

carl = NuevaTeacher(subject_taught='CS', ease=5)

carl.give_grade(mike_peller, 5)

# carl = Teacher(subject_taught='CS', ease=10)
# zob_romber = Teacher(subject_taught='Quebotics', ease=1)
# grades = [35, 62, 3, -17]
# pike_meller = Student(grades=grades)
#
#
# carl.give_grade(pike_meller, 5)
# zob_romber.give_grade(pike_meller, 5)
#
# print(pike_meller.grades)
