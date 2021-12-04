"""
Write a function that takes two strings and checks
to see if they are anagrams of each other.

For example:
"Army" and "Mary",
"Sharing" and "Sunday",
"Quid est veritas?" and "Vir est qui adest",
"Jim Morrison" and "Mr. Mojo Risin"
"Tom Marvolo Riddle" and "I am Lord Voldemort"
"""

import string


def anagram(str1, str2):
    str1 = str1.translate(str.maketrans('', '', string.punctuation)).lower()
    str2 = str2.translate(str.maketrans('', '', string.punctuation)).lower()
    if sorted(''.join(str1.split())) == sorted(''.join(str2.split())):
        return True
    else:
        return False


if __name__ == '__main__':

    string1 = input('Enter a string: ')
    string2 = input('Enter another string: ')
    print(f'The strings are anagrams: {anagram(string1, string2)}')
