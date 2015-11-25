class SimpleCar:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def __str__(self):
        return "{} {} built in: {}".format(self.make, self.model, self.year)


import csv
with open('car.csv', 'rb') as csvfile:
    carreader = csv.reader(csvfile, delimiter=',')
    cars = []
    for row in carreader:
        cars.append(SimpleCar(int(row[0]), row[1], row[2]))


for car in cars:
    if car.year >= 2016:
        print car