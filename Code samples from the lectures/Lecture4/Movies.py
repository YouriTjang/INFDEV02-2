class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def __str__(self):
        return "{}:  {}".format(self.title, self.rating)


