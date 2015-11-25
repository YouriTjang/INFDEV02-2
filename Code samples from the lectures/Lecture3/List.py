class Empty:
    def __str__(self):
        return "[]"

class Node:
    def __init__(self, x, xs):
        self.Value = x
        self.Tail = xs

    def __str__(self):
        return str(self.Value) + "->" + str(self.Tail)


lijst = Empty()
count = int(input("How many elements?"))
for i in range(0, count):
    element = int(input("Insert the next element"))
    lijst = Node(element, lijst)

print lijst

# einde = Empty()
# a = Node(1, einde)
# b = Node(2, a)
# c = Node(3, b)
# d = Node(4, c)
# e = Node(5, d)
# f = Node(6, e)
# print f

print abs(-1)