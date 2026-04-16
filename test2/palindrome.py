"""This program checks if a string is a palindrome."""


def palindrome(number):
    """This function checks if a string is a palindrome."""

    number = str(number)
    return number == number[::-1]


user_number = input('Enter a number: ')
print(palindrome(user_number))

assert palindrome(121)
assert not palindrome(-121)
assert not palindrome(10)
assert palindrome(0)
assert palindrome(1001)
assert not palindrome(100)
