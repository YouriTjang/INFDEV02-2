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

lijst = Empty()
for i in range(5):
    lijst = Node(i, lijst)
bewaarlijst = lijst

lijst2 = Empty()
while not lijst.IsEmpty:
    lijst2 = Node(lijst.Value, lijst2)
    lijst = lijst.Tail


while not lijst2.IsEmpty:
    print lijst2.Value
    lijst2 = lijst2.Tail