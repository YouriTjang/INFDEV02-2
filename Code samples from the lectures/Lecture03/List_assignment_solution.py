# Using python write a program.
    # read a list from the user input
    # make 3 functions that:
        #*removes all odd numbers
        #*sum all its values
        # reverses the list.

a = raw_input("insert any number").split(" ")
print a

def odd_number(odd):
    b = []
    for i in odd:
        if int(i) % 2 == 0:
            b.append(i)
    return b

print odd_number(a)

# *sum all the values using a loop
lijst = range(1, 11)
sum = 0
for getal in lijst:
    sum += getal
print sum

# reverses the list using a loop
lijst = "kaas"
print lijst
temp_list = []
for item in lijst[::-1]:
    # temp_list.append(item)
    temp_list += item
print temp_list



#* give the total amount of words in the list
#*give the average length of the words
# give the amount of words starting with:

word_list = open('OpenTaal-210G-basis-gekeurd.txt')

word_count = 0
a = 0
check_letter = "a"
letter_count = []
for i in range(26):
    letter_count.append(0)

for word in word_list:
    letter = word[0].lower()
    if 'a' <= letter <= 'z':
        index_letter = ord(letter) - ord("a")
        letter_count[index_letter] += 1

for i in letter_count:
    print i
