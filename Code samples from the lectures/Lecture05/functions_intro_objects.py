class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return "Name: {} ({})".format(self.name, self.grade)


def plus_one(student):
    student.grade += 1
    return student.grade


student1 = Student("Faas de Bruyn", 9)
student2 = student1

plus_one(student1)
print student2