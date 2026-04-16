"""
This program adds 1 to a number represented as a list of digits.
"""


def add_one(number):
    """
    Adds 1 to a number represented as a list of digits.
    Returns a new list with the result.
    """

    result = number[:]
    result.reverse()

    rest = 1

    for i in range(len(result)):  # pylint: disable=consider-using-enumerate
        if rest == 0:
            break

        result[i] += rest

        if result[i] == 10:
            result[i] = 0
            rest = 1
        else:
            rest = 0

    if rest == 1:
        result.append(1)

    result.reverse()
    return result


print(add_one([1, 2, 3]))
print(add_one([1, 2, 9]))
print(add_one([9, 9, 9]))
