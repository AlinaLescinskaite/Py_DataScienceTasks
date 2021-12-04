"""
Create a function that checks that the string given as an argument
is a palindrome (ie read backwards and forwards is exactly the same, eg
"kayak", "madam").
"""


def palindrome(word):

    return word == word[::-1]


if __name__ == '__main__':

    input_word = input('Enter a word: ')
    is_palindrome = palindrome(input_word)
    print(f'{input_word} is palindrome: {is_palindrome}')
