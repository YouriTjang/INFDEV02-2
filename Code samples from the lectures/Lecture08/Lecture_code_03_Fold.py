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


def fold(list, function, start_value):
    if list.IsEmpty:
        return start_value
    else:
        return function(list.Value, fold(list.Tail, function, start_value))


# example
list = Node(9, Node(7, Node(2, Empty())))

print(fold(list, lambda x, y: x+y, 0))
