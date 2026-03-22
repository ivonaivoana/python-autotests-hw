"""
This program finds the number that is radially opposite
to a given number on a circle of integers from 0 to n-1.
"""


def solution(n, first_number):
    """
        Returns the number opposite to `first_number`
        on a circle of size `n`.
        """

    clocks = list(range(0, n))
    first_half = clocks[:n//2]
    second_half = clocks[n//2:]
    combined = list(zip(first_half, second_half))

    if first_number in first_half:
        return combined[first_half.index(first_number)][1]
    else:
        return combined[second_half.index(first_number)][0]


assert solution(10, 6) == 1
assert solution(10, 2) == 7
assert solution(10, 4) == 9
print('ok')
