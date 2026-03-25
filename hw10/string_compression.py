"""
String compression module.
"""


def solution(text):
    """
    Compress consecutive duplicate characters in a string.

    Args:
        text: Input string.

    Returns:
        Compressed string with character counts for repeated chars.
    """

    count = 1
    result = ''
    if len(text) == 1:
        return text
    else:
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count += 1
            else:
                result += text[i-1]
                if count > 1:
                    result += str(count)
                count = 1
        result += text[-1]
        if count > 1:
            result += str(count)
    return ''.join(result)


assert solution("cccbba") == "c3b2a"
assert solution("abeehhhhhccced") == "abe2h5c3ed"
assert solution("aaabbceedd") == "a3b2ce2d2"
assert solution("abcde") == "abcde"
assert solution("aaabbdefffff") == "a3b2def5"
