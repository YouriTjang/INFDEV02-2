class Empty:
  def __init__(self):
    self.IsEmpty = True
Empty = Empty()

class Node:
  def __init__(self, x, xs):
    self.IsEmpty = False
    self.Value = x
    self.Tail = xs


cnt = int(input("How many elements?"))
l = Empty
for i in range(0, cnt):
  l = Node(i, l)

x = l
while not(x.IsEmpty):
  print(x.Value)
  x = x.Tail

x = l
lEven = Empty
while not(x.IsEmpty):
  if x.Value % 2 == 0:
    lEven = Node(x.Value, lEven)
  x = x.Tail

print("~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~")

x = lEven
while not(x.IsEmpty):
  print(x.Value)
  x = x.Tail

quit()

def printList(l):
  if(l.IsEmpty):
    return Empty
  else:
    print(l.Head)
    printList(l.Tail)

def map(l, f):
  if(l.IsEmpty):
    return Empty
  else:
    return Node(f(l.Head), map(l.Tail, f))

def filter(l, p):
  if(l.IsEmpty):
    return Empty
  else:
    if p(l.Head):
      return Node(l.Head, filter(l.Tail, p))
    else:
      return filter(l.Tail, p)

def fold(l, f, z):
  if(l.IsEmpty):
    return z
  else:
    return f(l.Head, fold(l.Tail, f, z))

l = Node(1, Node(2, Node(3, Node(4, Empty))))
#printList(map(Node(1, Node(2, Node(3, Node(4, Empty)))), lambda x: x + 1))
#printList(filter(Node(1, Node(2, Node(3, Node(4, Empty)))), lambda x: x % 2 == 0))
#print(fold(Node(1, Node(2, Node(3, Node(4, Empty)))), lambda x, y: x + y, 0))
#print(fold(l, max, float('-inf')))
#print(fold(l, min, float('inf')))

printList(fold(Node(1, Node(2, Node(3, Node(4, Empty)))), lambda x, y: Node(x+1,y), Empty))
#printList(fold(Node(1, Node(2, Node(3, Node(4, Empty)))), lambda x, y: Node(x, y) if x % 2 == 0 else y, Empty))

