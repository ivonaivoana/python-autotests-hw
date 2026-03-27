"""
Candle burning module with leftovers recycling.
"""


def solution(candle_number, make_new):
    """
    Calculate total candles that can be burned when
    leftovers can be combined into new candles.

    Args:
        candle_number (int): Initial number of candles.
        make_new (int): Number of leftovers needed to create one new candle.

    Returns:
        int: Total number of candles that can be burned.
    """

    candle_used = candle_number
    leftovers = candle_number
    while leftovers >= make_new:
        x = leftovers // make_new
        candle_used += x
        leftovers = leftovers - x * make_new + x
    return candle_used


assert solution(5, 2) == 9
assert solution(1, 2) == 1
assert solution(15, 5) == 18
assert solution(12, 2) == 23
assert solution(6, 4) == 7
assert solution(13, 5) == 16
assert solution(2, 3) == 2
