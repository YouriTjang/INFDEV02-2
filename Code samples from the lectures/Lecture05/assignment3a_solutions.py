
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def assignment1():
    number = 300
    while number != 1:
        number = collatz(number)
        print(number)


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

def append(value, lijst):
    return Node(value, lijst)

def delete(lijst2, value):
    lijst = lijst2
    while not lijst.IsEmpty:
        if lijst.Value == value:
            previous.Tail = lijst.Tail
        previous = lijst
        lijst = lijst.Tail
    return lijst

def list_range(n):
    lijst = Empty()
    for value in range(n):
        lijst = append(value, lijst)
    return lijst

lijst = list_range(9)
print(lijst)
delete(lijst, 5)
print(lijst)