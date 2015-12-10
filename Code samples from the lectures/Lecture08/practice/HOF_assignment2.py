import csv

class Empty:
    def __init__(self):
        self.IsEmpty = True

    def __str__(self):
        return "[]"

class Node:
    def __init__(self, x, xs):
        self.IsEmpty = False
        self.Value = x
        self.Tail = xs

    def __str__(self):
        return str(self.Value) + "->" +str(self.Tail)


class Movie:
    def __init__(self, id, title, year):
        self.id = id
        self.title = title
        self.ratings = Empty()
        self.year = year
        self.genres = Empty()

    def __str__(self):
        return "{} - {} - {}".format(self.id, self.title, self.year, self.genres)

def read_movies():
    print("reading movies.csv")
    movies = Empty()
    with open('movies.csv', encoding='utf8') as csvfile:
        movie_reader = csv.reader(csvfile, delimiter=',')
        movie_reader.__next__()  # this skips the header

        #iterate the movie file
        for row in movie_reader:
            #make a movie with: id, title, year
            movie = Movie(int(row[0]), row[1][:-6], row[1][-5:-1])

            #add a list of genres
            genres = row[2].split("|")
            for g in genres:
                movie.genres = Node(g, movie.genres)

            #add the movie to the list of movies
            movies = Node(movie, movies)
    return movies


def find(movies, movie_id):
    while not movies.IsEmpty:
        if movies.Value.id == movie_id:
            return movies
        movies = movies.Tail
    return None

def add_ratings_to_movies(movies):
    with open('ratings.csv', encoding='utf8') as csvfile:
        rating_reader = csv.reader(csvfile, delimiter=',')
        rating_reader.__next__()  # this skips the header

        #iterate the rating file
        for row in rating_reader:
            movies_find_start = movies
            movie_reference = find(movies_find_start, int(row[1]))
            if movie_reference is not None:
                movie_reference.Value.ratings = Node(float(row[2]), movie_reference.Value.ratings)
    return movies

# Read the movies.csv file into a list of movie-objects
movies = read_movies()
# Read the ratings.csv file and add each rating to the corresponding movie
complete_movies = add_ratings_to_movies(movies)



def map(list, function):
    if (list.IsEmpty):
        return Empty()
    else:
        return Node(function(list.Value), map(list.Tail, function))

def filter(list, function):
    if list.IsEmpty:
        return Empty()
    else:
        if function(list.Value):
            #add the value
            return Node(list.Value, filter(list.Tail, function))
        else: #skip the value
            return filter(list.Tail, function)

def fold(list, function, start_value):
    if list.IsEmpty:
        return start_value
    else:
        return function(list.Value, fold(list.Tail, function, start_value))



# Example: filter on all titles starting with 'A'
movielist_starting_with_a = filter(complete_movies, lambda movie: movie.title[0] == 'A' )
print(movielist_starting_with_a)

# Exercise 1
# Filter the movies on the year 1994, and print
# This should show none of the movies
#
# Filter the movies on the year 1995, and print
# This should show all of the movies, sorry this
# small data smample only contains 1995-movies


# Exercise 2
# Each movie-object contains a list of genres
# Filter the movies with the genre 'animation'
#
# Filter the movies with the genres 'comedy' and 'romance'

# Exercise 3
# Calculate the amount of movies that are comedy romances

# Exercise 4
# calculate the average rating for each movie
