"""
Create a function that checks that the number given in the argument
is prime. The function should take a numeric value and return a logical
value of True / False.

E.g.
For 11 the function will return True, for 12 -> False.
"""


def prime_number(number):

    number = int(number)
    if number == 0 or number == 1:
        return False

    for i in range(2, int(number/2)+1):
        if (number % i) == 0:
            return False

    return True


if __name__ == '__main__':

    input_num = input('Enter a number: ')
    prime = prime_number(input_num)
    print(f'{input_num} is prime: {prime}')
