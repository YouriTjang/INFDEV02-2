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


def filter(list, function):
    if list.IsEmpty:
        return Empty()
    else:
        if function(list.Value):
            #add the value
            return Node(list.Value, filter(list.Tail, function))
        else: #skip the value
            return filter(list.Tail, function)

#example
list = Node(9, Node(7, Node(2, Empty())))

print(filter(list, lambda x: x % 2 == 1))

