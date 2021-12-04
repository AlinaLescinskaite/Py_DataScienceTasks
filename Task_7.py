"""
Write a function that will return the 5 most common words from
Mickiewicz's work. https://pastebin.com/raw/aAHeW5Pt (copy and save
to a text file what you will find at this link).

Hint: use the open() function, split() method, dictionary and loop.
"""

import string

if __name__ == '__main__':

    f = open('Mickiewicz.txt')
    counts = dict()
    for line in f:
        line = line.translate(str.maketrans('', '', string.punctuation)).lower()
        words = line.split()
        for i in words:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1

    word_list = list()
    for key, val in list(counts.items()):
        word_list.append((val, key))

    word_list.sort(reverse=True)
    print(word_list[:5])

