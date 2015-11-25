import csv
import time

class Node:
    def __init__(self, value, tail):
        self.value = value
        self.tail = tail
        self.isEmpty = False

class Empty:
    def __init__(self):
        self.isEmpty = True


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
    while not movies.isEmpty:
        if movies.value.id == movie_id:
            return movies
        movies = movies.tail
    return None

def calc_rating(rating_sum, rating_count):
    return  rating_sum/rating_count if rating_count > 0 else 0


def read_movies():
    print "reading movies.csv"
    movies = Empty()
    with open('movies.csv', 'rb') as csvfile:
        movie_reader = csv.reader(csvfile, delimiter=',')
        movie_reader.next()  # this skips the header
        for row in movie_reader:
            # movies.append(Movie(int(row[0]), row[1]))
            movies = Node(Movie(int(row[0]), row[1]), movies)
    return movies


def add_ratings_to_movies(movies):
    with open('ratings.csv', 'rb') as csvfile:
        rating_reader = csv.reader(csvfile, delimiter=',')
        rating_reader.next()  # this skips the header
        for row in rating_reader:
            rating = Rating(int(row[1]), float(row[2]))
            movies_find_start = movies
            movie_reference = find(movies_find_start, rating.movie_id)
            movie_reference.value.rating_count += 1
            movie_reference.value.rating_sum += rating.rating
    return movies


t0 = time.clock()
t00 = time.clock()

movies = read_movies()

movies_start = movies
print (time.clock() - t00)/60.0, "minutes to building movielist"
t00 = time.clock()

print "reading ratings.csv"
add_ratings_to_movies(movies)

print (time.clock() - t00)/60.0, "minutes to summing ratings"
t00 = time.clock()


# for movie in sorted(movies, key=lambda m : calc_rating(m.rating_sum, m.rating_count) ):
#     print movie

# for movie in sorted(movies, key=lambda m : m.rating_count ):
#     print movie + " -- " + movie.rating_count

movies = movies_start
while not movies.isEmpty:
    print movies.value
    movies = movies.tail

print (time.clock() - t0)/60.0, "minutes process time"