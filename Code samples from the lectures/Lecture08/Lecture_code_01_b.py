# 1
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    return False
f1 = monkey_trouble(True, False)
print(f1)

# 2
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def __str__(self):
        return "{} - {}".format(self.title, self.rating)

def getRating(m):
    return m.rating

movie = Movie("The peanuts movie", "7.8")
f2 = getRating(movie)
print(f2)


#3
def combine(f, x, y):
    return f(x, y)

f3 = combine(monkey_trouble, True, True)
print(f3)
