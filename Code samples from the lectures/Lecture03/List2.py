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

lijst = Empty()
for i in range(0, 5):
    element = 5-i
    lijst = Node(element, lijst)

def print_lijst(lijst):
    x = lijst
    while not x.IsEmpty:
        print x.Value
        x = x.Tail

