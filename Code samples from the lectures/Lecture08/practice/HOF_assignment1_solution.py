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

def map(list, function):
    if (list.IsEmpty):
        return Empty()
    else:
        return Node(function(list.Value), map(list.Tail, function))

def filter(list, function):
    if list.IsEmpty:
        return Empty()
    else:
        if function(list.Value):
            #add the value
            return Node(list.Value, filter(list.Tail, function))
        else: #skip the value
            return filter(list.Tail, function)

def fold(list, function, start_value):
    if list.IsEmpty:
        return start_value
    else:
        return function(list.Value, fold(list.Tail, function, start_value))


class Car:
    def __init__(self, id, position):
        self.id = id
        self.position = position

road = Node("a", Node("b", Node("c", Empty())))
car1 = Car(1, road)
car2 = Car(2, road)
car3 = Car(3, road)

cars = Node(car1, Node(car2, Node(car3, Empty())))

