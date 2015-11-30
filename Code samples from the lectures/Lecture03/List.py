class Empty:
    def __init__(self):
        self.isEmpty = True

    def __str__(self):
        return "[]"

class Node:
    def __init__(self, x, xs):
        self.Value = x
        self.Tail = xs
        self.isEmpty = False

    def __str__(self):
        return str(self.Value) + "->" + str(self.Tail)


lijst = Empty()

lijst = Node(1, lijst)
lijst = Node(2, lijst)
lijst = Node(3, lijst)
lijst = Node(4, lijst)
lijst = Node(5, lijst)
lijst = Node(6, lijst)

while not lijst.isEmpty:
    print lijst.Value
    lijst = lijst.Tail