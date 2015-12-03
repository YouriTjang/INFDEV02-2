# Using python write a program.
    # read a list from the user input
    # make 3 functions that:
        # removes all odd numbers
        # sum all its values
        # reverses the list.

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


lijst = Empty()
for i in range(9):
    lijst = Node(i, lijst)

lijst2 = Empty()
while not lijst.IsEmpty:
    if lijst.Value % 2 == 0:
        lijst2= Node(lijst.Value, lijst2)
    lijst = lijst.Tail
print lijst2

lijst3 = lijst2
som = 0
while not lijst2.IsEmpty:
    som += lijst2.Value
    lijst2 = lijst2.Tail
print som

#reverse the list
lijst4 = Empty()
while not lijst3.IsEmpty:
    lijst4 = Node( lijst3.Value, lijst4)
    lijst3 = lijst3.Tail
print lijst4


word_list = open('OpenTaal-210G-basis-gekeurd.txt')

words = Empty()
size = 0
word_length = 0
for word in word_list:
    words = Node(word, words)
    size += 1
    word_length += len(word)

print "Average word length: " + str(word_length/size)