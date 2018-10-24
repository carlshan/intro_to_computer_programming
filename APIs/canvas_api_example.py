from canvasapi import Canvas

API_URL = "https://nuevaschool.instructure.com/"
API_KEY = "5296~IhwOEHJT3VvEToL02fOMSI6NmnRtWZBxozPY2CjvAoKolj41jMN0jG2EMWcJt7Zd"

canvas = Canvas(API_URL, API_KEY)

course = canvas.get_course(1571)

assignments = course.get_assignments()

for assignment in assignments:
    print(assignment.due_at)
