
#*read a list from the user input
    # make 3 functions that:
        #*removes all odd numbers
        #*sum all its values
        # reverses the list.

aantal =  input("hoeveel nummers wil je opslaan?")
lijst = []
for i in range(aantal):
    lijst.append(input("geef een nummer"))

print lijst

for i in lijst:
    if i % 2 != 0:
        lijst.remove(i)

print lijst

sum = 0
for i in lijst:
    sum += i
print sum

lijst = [1,2,3,4,5,6,7,8,9,0]
lijst2 = []
for i in range(len(lijst)):
    lijst2.append( lijst[len(lijst)-i-1] )

print lijst2








