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


def vul_loop():
    lijst = Empty()
    for i in range(0, 5):
        element = 5-i
        lijst = Node(element, lijst)
    return lijst

def iterate():
    lijst = vul_loop()
    x = lijst
    while not x.IsEmpty:
        print x.Value
        x = x.Tail

iterate()