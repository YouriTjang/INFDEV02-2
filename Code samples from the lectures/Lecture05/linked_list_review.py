
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
        return str(self.Value) + "->" + str(self.Tail)


def range(start, end):
    lijst = Empty()
    while start <= end:
        end -= 1
        lijst = Node(end, lijst)
    return lijst

print(range(1, 10))

