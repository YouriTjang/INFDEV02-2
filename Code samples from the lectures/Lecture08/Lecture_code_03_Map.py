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


def map(l, f):
    if (l.IsEmpty):
        return Empty()
    else:
        return Node(f(l.Value), map(l.Tail, f))

#example map
list = Node(9, Node(7, Node(2, Empty())))

print(map(list, lambda x: x + 1))
print(map(list, lambda x: "hallo" + str(x)))
