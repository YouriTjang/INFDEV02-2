# Q1
#Fill a linked list with your name and 2 other names. Use these classes:


class Empty:
    def __init__(self):
        self.IsEmpty = True

class Node:
    def __init__(self, x, xs):
        self.IsEmpty = False
        self.Value = x
        self.Tail = xs

# Q2
# define a movie class with the following attributes: the title, a list of ratings, and a list of genres
# instantiate 1 object with made up values


# Q3
# Given the following function denition and a sample call, show stack and heap at all steps of the computation.


def foo(n):
    if n == 1:
        return 1
    else:
        return foo(n - 1)

print(foo(3))


# Q4
# Define a recursive 'range' function to create a custom list (only use Empty and Node)
# with all the elements between two given numbers.
