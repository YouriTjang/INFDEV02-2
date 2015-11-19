
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade  = grade

    def __str__(self):
        return "{} - {}".format(self.name, self.grade)

students = []
students.append(Student("Nienke van de Wal", 5))
students.append(Student("Owen Blonk", 6))
students.append(Student("Aron Knoers", 1))
students.append(Student("Noud Vermeulen", 10))
students.append(Student("Lieke van Breukelveen-Jonkman", 8))
students.append(Student("Benjamin Pratt", 2))
students.append(Student("Gerrit Erhout-van Dokkum", 7))
students.append(Student("Merijn der Kijnder", 9))
students.append(Student("Iris Govarts", 1))
students.append(Student("Mick de Heer", 10))
students.append(Student("Mees Willemsen", 2))
students.append(Student("Rens Genefaas", 4))
students.append(Student("Mirte Luster", 5))
students.append(Student("Jamie Mercks-Goedhart", 2))
students.append(Student("Tyler Bertho-Smits", 6))
students.append(Student("Danique Adriaense-van der Steen", 4))
students.append(Student("Fiene Heijmans", 2))
students.append(Student("Elize van Mook-Haneberg", 1))
students.append(Student("Noud Rackham", 2))
students.append(Student("Yasmin van Beaumont", 8))
students.append(Student("Ryan Kamp", 5))
students.append(Student("Jay van den Berg", 7))
students.append(Student("Selena Scheffers", 5))
students.append(Student("Stef van Laar", 4))
students.append(Student("Jay Elsenaar", 4))
students.append(Student("Yfke Lelijveld", 7))

sum = 0
for student in students:
    sum += student.grade
print sum / len(students)

print len(students)

for i in range(9):
    print i

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
    print i
