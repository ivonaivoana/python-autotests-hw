"""
String processing module deleting the symbols before the #.
"""


def solution(string):
    """
    Remove character before each '#' in the string.

    Args:
        string (str): Input string.

    Returns:
        str: Processed string.
    """

    result = []
    for char in string:
        if char == '#':
            if result:
                result.pop()
        else:
            result.append(char)
    return ''.join(result)


assert solution("a#bc#d") == "bd"
assert solution("abc#d##c") == "ac"
assert solution("abc##d######") == ""
assert solution("#######") == ""
assert solution("") == ""
