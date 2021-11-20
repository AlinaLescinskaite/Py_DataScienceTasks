"""
Write a program that will convert the sequence of numbers
entered by the user into text, e.g.:

112 -> "one one two"
9973 -> "nine nine seven three"

Hint: you need the input () function, a dictionary and a loop.
"""


if __name__ == '__main__':

    num_sequence = input("Enter a sequence of numbers: ")
    # print(num_sequence)

    num_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
                5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

    # option 1:
    digits = [num_dict[int(i)] for i in str(num_sequence)]
    num_string = ' '.join(digits) # list to string
    print(num_string)

    # option 2:
    digits = []
    for i in str(num_sequence):
        digits.append(num_dict[int(i)])
    num_string = ' '.join(digits) # list to string
    print(num_string)