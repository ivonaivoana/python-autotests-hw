"""
Credit card validator based on the Luhn algorithm.

Validates whether a given number can be a real credit card number.
Returns False for invalid or non-numeric input.
"""


def solution(number):
    """
    Check if a credit card number is valid using the Luhn algorithm.
    Args:
        number (int or str): Credit card number.
    Returns:
        bool: True if valid, False otherwise.
    Raises:
        ValueError: If input is not a non-empty number.
    """

    number_str = str(number).strip()
    if not number_str.isdigit() or len(number_str) == 0:
        return False

    digits = [int(d) for d in number_str[::-1]]
    total = 0
    for idx, d in enumerate(digits):
        if idx % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


assert not solution(4561261212345464)
assert solution(4561261212345467)
assert solution(378282246310005)
assert solution(371449635398431)
assert solution(378734493671000)
assert solution(5610591081018250)
assert solution(30569309025904)
assert solution(38520000023237)
assert solution(6011111111111117)
assert solution(6011000990139424)
assert solution(3530111333300000)
assert solution(3566002020360505)
assert solution(5555555555554444)
assert solution(5105105105105100)
assert solution(4111111111111111)
assert solution(4012888888881881)
assert solution(4222222222222)
assert not solution(76009244561)
assert solution(5019717010103742)
assert solution(6331101999990016)
assert not solution("QWERTYU")
assert not solution(None)
assert not solution(" ")
print('All checks have been completed successfully.')
