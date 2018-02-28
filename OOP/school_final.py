class Teacher:

    def __init__(self, name, nickname, subject, awesomeness):
        self.name = name
        self.nickname= nickname
        self.subject = subject
        self.awesomeness = awesomeness


    def give_score(self, student, score):
        student.scores.append(score)


    def eat_peanut_butter(self):
        print("Mmmmm. My nickname is {} and I like peanut butter".format(self.nickname))
        print('\n')
        print("I'm eating some right now!")


class Student):

    def __init__(self, name, grade, scores=[]):
        self.name = name
        self.grade = grade
        self.scores = scores


    def favorite_teacher(self, teacher):
        favorite_teacher = teacher.nickname
        favorite_subject = teacher.subject
        print('My favorite teacher is: {}'.format(favorite_teacher))
        print('And this teacher teaches: {}'.format(favorite_subject))


    def average_score(self):
        total = 0
        for score in self.scores:
            total += score

        averaged = total / len(self.scores)
        print("My average score is {}".format(averaged))
        return averaged


carl = Teacher(name='Carl', nickname='Octopants', subject='Computer Science')
print("Hi, I'm a teacher and my name is {}".format(carl.nickname))

jenny =  Student(name='Jenny', grade=7, scores=[100, 90, 80])
print("Hi, I'm a student and my name is {}".format(jenny.name))
jennys_average = jenny.average_score()
print("My average score in {}'s class is {}".format(carl.nickname, jennys_average))

print("{} did well on an assignment! I'm going to give her a new score.".format(jenny.name))
carl.give_score(jenny, 100)

new_average = jenny.average_score()
print("Yay! Now my average score is {}".format(new_average))
