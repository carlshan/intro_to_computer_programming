# Why do we use classes?
# For all sorts of reasons that may not be obvious right now.
# 1. To create our own blueprints of ideas that don't currently exist.
# 2. To "bind" certain functions to certain objects. That way, it's less likely
# to cause bugs in the future.
# 3. It forces you to plan more, so you have a deeper planning phase
# 4. It allows you to create a hierarchy between ideas and objects (inheritance)

# At the end of the day you don't NEED to understand how to write classes to understand
# the rest of the curriculum.

from TeacherFile import Teacher
from StudentFile import Student

a_teacher = Teacher(name='Carl')
a_student = Student(name='Liam', grade=9)

a_teacher.introduce()
a_student.introduce()
