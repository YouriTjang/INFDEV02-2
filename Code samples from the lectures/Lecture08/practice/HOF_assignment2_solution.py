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

# Of
list_of_rating_lists = map(movielist_starting_with_a, lambda movie: movie.ratings)

def average(list):
    sum = fold(list, lambda x,y: x+y, 0)
    cnt = fold(list, lambda x,y: 1+y, 0)
    if cnt == 0:
        return 0
    return sum/cnt

averages = map(list_of_rating_lists, lambda ratings: average(ratings))
print(averages)

#your turn:
#print all the movies

