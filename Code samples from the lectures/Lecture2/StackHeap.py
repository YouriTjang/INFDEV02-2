class Student:
    def __init__(self, number):
        self.number = number

s1 = Student(1)
s2 = s1
s3 = Student(3)

s2.number += 1

print s1.number
print s2.number
print s3.number