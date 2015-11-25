# abstraction movie:
#     id, a unique number;
#     title, a string;
#     rating, a number;

class movie:
    def __init__(self, id, title, rating):
        self.id = id
        self.title = title
        self.rating = rating

def max(lijst):
    max = None
    for i in lijst:
        if i > max:
            max = i
    return max

print max([-1,-2,-3,-4,-5,-6,-67])
