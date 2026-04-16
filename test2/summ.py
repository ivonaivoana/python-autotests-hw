"""
This program calculates the summ of
all digits in the set number
"""


def summ_of_all_digits(number):
    """ Calculates the sum of all digits
    in the set number """

    total = 0
    for digit in range(1, number + 1):
        total += digit
    return total


assert summ_of_all_digits(1) == 1
assert summ_of_all_digits(8) == 36
assert summ_of_all_digits(22) == 253
assert summ_of_all_digits(100) == 5050
