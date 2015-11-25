
class Movie:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __str__(self):
        return self.id + self.title


import csv
with open('movies.csv', 'rb') as csvfile:
    movie_reader = csv.reader(csvfile, delimiter=',')
    movie_reader.next() #this skips the header
    movies = []
    for row in movie_reader:
        movies.append(Movie(int(row[0]), row[1]))
