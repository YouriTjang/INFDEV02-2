#Draw the stack and the heap for each step of the next program
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    # def __str__(self):
    #     return "{} - {}".format(self.name , self.grade)

s1 = Student("Maarten van Geest-Wolters", 7)
s2 = s1

s2.grade = 10
print(s1)
print(s2)


#Draw the stack and heap for the next program
a = 2
def plus_one(b):
    result = b + 1
    a = 1
    return result

a = 5
b = plus_one(a)
print(a)
print(b)