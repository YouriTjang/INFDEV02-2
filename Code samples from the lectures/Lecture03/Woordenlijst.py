
word_list = open('OpenTaal-210G-basis-gekeurd.txt')

words = []
size = 0
for word in word_list:
    size += 1
    words.append(word)
print size

word_length = 0
for word in words:
    word_length += len(word)
print word_length
print word_length/size


word_count = []
for let in range(26):
    word_count.append(0)

for word in words:
    first_letter = word[0].lower()
    letter_index = ord(first_letter) - ord('a')
    if(0 < letter_index < 26):
        word_count[letter_index] += 1

for count in word_count:
    print count
