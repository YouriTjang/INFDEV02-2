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
for i in range(5):
    lijst = Node(i, lijst)
bewaarlijst = lijst
print lijst

lijst_met_oneven_nummers = Empty()
while not lijst.IsEmpty:
    if lijst.Value % 2 == 0:
        lijst_met_oneven_nummers = Node(lijst.Value, lijst_met_oneven_nummers)
    lijst = lijst.Tail

print lijst_met_oneven_nummers

som = 0
bewaarlijst = lijst_met_oneven_nummers
while not lijst_met_oneven_nummers.IsEmpty:
    som += lijst_met_oneven_nummers.Value
    lijst_met_oneven_nummers = lijst_met_oneven_nummers.Tail

print som

r_lijst = Empty()

while not bewaarlijst.IsEmpty:
    r_lijst = Node(bewaarlijst.Value, r_lijst)
    bewaarlijst = bewaarlijst.Tail

print r_lijst


word_list = open('OpenTaal-210G-basis-gekeurd.txt')

words = Empty()
size = 0
word_length = 0
for word in word_list:
    size += 1
    word_length += len(word)
    words = Node(word, words)

print word_length / size