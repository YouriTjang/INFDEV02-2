# 1
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    return False



# 2
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

def getRating(m):
    return m.rating





#3
def combine(f, x, y):
    return f(x, y)
