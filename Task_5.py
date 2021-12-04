"""
Create a function that will calculate the number of upper and lower
case letters in a string.

eg for: "The quick Brown Fox"

expected result:
Number of uppercase letters: 3, number of lowercase letters : 13

Hint: use a loop, conditional statement, and appropriate methods
for the string.
"""


def upper_lower_case(string):

    upper = 0
    lower = 0
    for i in string:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1

    return lower, upper


if __name__ == '__main__':

    input_str = input("Enter a string: ")
    low, up = upper_lower_case(input_str)

    print(f'Number of uppercase letters: {up} \n'
          f'Number of lowercase letters : {low}')
