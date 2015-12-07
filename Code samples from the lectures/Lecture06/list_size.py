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


def recursive_list_size(lijst2):
    lijst = lijst2
    if lijst.isEmpty:
        return 0
    else:
        return 1 + recursive_list_size(lijst.Tail)

def print_list(lijst2):
    lijst = lijst2
    if lijst.isEmpty:
        print("[]")
    else:
        print(lijst.Value," -> ", end="")
        print_list(lijst.Tail)


def append(value, lijst):
    return Node(value, lijst)


def list_range(n):
    lijst = Empty()
    for value in range(n):
        lijst = append(value, lijst)
    return lijst

lijst = list_range(10)
print_list(lijst)
print( size(lijst) )
print( recursive_list_size(lijst) )

