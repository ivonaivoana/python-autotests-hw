"""
There are two functions square() and parity()
in this file.
"""


def square():
    """Return the square of the given number"""

    number = int(input('Enter the number: '))
    return number ** 2


def parity():
    """Return whether the number is even or odd"""

    number = int(input('Enter the number: '))
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"


print(square())
print(parity())
