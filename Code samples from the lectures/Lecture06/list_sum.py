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

def size(lijst2):
    lijst = lijst2
    result = 0
    while not lijst.isEmpty:
        result += 1
        lijst = lijst.Tail
    return result

def rec_size(lijst):
