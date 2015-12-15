#Fill a linked list with your name and 2 other names. Use these classes:
class Empty:
    def __init__(self):
        self.empty = True

    def __str__(self):
        return "[]"


class Node:
    def __init__(self, value, tail):
        self.empty = False
        self.value = value
        self.tail = tail

    def __str__(self):
        return str(self.value) + "->" + str(self.tail)


dev_team = Node("Guiseppe", Node("Tony", Node("Youri", Node("Ahmad", Node("Mohammed", Empty())))))


# define a movie class with the following attributes: the title, a list of ratings, and a list of genres
# instantiate 1 object with made up values
class Movie:
    def __init__(self, title, ratings, genres):
        self.title = title
        self.ratings = ratings
        self.genres = genres

m = Movie("The peanuts movie", Node(8, Node(2, Node(10, Empty()))), ["Animation", "Comedy", "Adventure"])


# Given the following function definition and a sample call, show stack and heap at all steps of the computation.
def foo(n):
    if n == 1:
        return 1
    else:
        return foo(n - 1)

print(foo(3))

# pc  foo
# 33  nil
#
# pc  foo pc  n foo
# 33  nil 31  3 nil
#
# pc  foo pc  n foo   pc  n foo
# 33  nil 31  3 nil   31  2 nil
#
# pc  foo pc  n foo   pc  n foo   pc  n   return
# 33  nil 31  3 nil   31  2 nil   31  1   1
#
# pc  foo pc  n foo   pc  n foo
# 33  nil 31  3 nil   31  2 1
#
# pc  foo pc  n foo
# 33  nil 31  3 1
#
# pc  foo
# 33  1


# Define a recursive 'range' function to create a custom list (only use Empty and Node)
# with all the elements between two given numbers.
def range(start, end):
    if start == end:
        return Empty()
    else:
        return Node(start, range(start+1, end))

print(range(1, 4))