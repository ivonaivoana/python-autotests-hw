"""
Module for converting a string into a mirrored (palindromic)
form based on a given limit.
"""


def string_converter(string, limit):
    """
    Creates a palindrome from the first `limit` characters of a string.
    """

    result = string[:limit] + string[:limit-1][::-1]
    return result


print(string_converter("qwerty", 2))
print(string_converter("qwerty", 4))
