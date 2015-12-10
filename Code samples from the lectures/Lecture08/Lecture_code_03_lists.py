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
        return str(self.Value) + "->" +str(self.Tail)


# wat we voorheen deden:
list = Node(9, Node(7, Node(2, Empty())))

# filteren
while not list.IsEmpty:
    if list.Value % 2 == 0:
        print(list.Value)
    list = list.Tail

# per Node iets doen
list2 = Empty()
while not list.IsEmpty:
    list2 = Node(list.Value * 3, list2)
    list = list.Tail


sum = 0
while not list.IsEmpty:
    sum += list.Value
    list = list.Tail

