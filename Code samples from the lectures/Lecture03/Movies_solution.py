import csv
import time


class Movie:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.rating_count = 0.0
        self.rating_sum = 0

    def __str__(self):
        rating = 0
        if self.rating_count > 0:
            rating = self.rating_sum/self.rating_count

        return "{} - {} - {}".format(self.id, self.title, rating)

class Rating:
    def __init__(self, movie_id, rating):
        self.movie_id = movie_id
        self.rating = rating


def find(movies, movie_id):
    for i in range(len(movies)):
        if movies[i].id == movie_id:
            return i
    return 0

t0 = time.clock()
print "reading movies.csv"
with open('movies.csv', 'rb') as csvfile:
    movie_reader = csv.reader(csvfile, delimiter=',')
    movie_reader.next() #this skips the header
    movies = []
    for row in movie_reader:
        movies.append(Movie(int(row[0]), row[1]))

print "reading ratings.csv"

with open('ratings.csv', 'rb') as csvfile:
    rating_reader = csv.reader(csvfile, delimiter=',')
    rating_reader.next() #this skips the header
    for row in rating_reader:
        rating = Rating(int(row[1]), float(row[2]))
        movie_index = find(movies, rating.movie_id)
        movies[movie_index].rating_count += 1
        movies[movie_index].rating_sum   += rating.rating

def calc_rating(rating_sum, rating_count):
    return  rating_sum/rating_count if rating_count > 0 else 0

# for movie in sorted(movies, key=lambda m : calc_rating(m.rating_sum, m.rating_count) ):
#     print movie

for movie in sorted(movies, key=lambda m : m.rating_count ):
    print movie + " -- " + movie.rating_count


print (time.clock() - t0)/60.0, "minutes process time"

