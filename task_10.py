"""
Write a program that returns the absolute value of a number retrieved
from the user. The program should keep asking for this number until it is
correctly given.

Remember that the user may not always enter a numeric value, but may
also enter, for example, "cauliflower". Check what happens then and be
sure to handle exceptions.
"""

if __name__ == '__main__':

    while True:
        try:
            user_input = int(input("Enter a number: "))
            break
        except ValueError:
            print("Enter a digit")
            continue

    print(f"number: {abs(user_input)}")
