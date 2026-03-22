"""
This program checks if while a != b: a+=1; b-=1 loops infinitely.
Returns:
    True if infinite loop, False otherwise.
"""

users_a = int(input("Enter a: "))
users_b = int(input("Enter b: "))


def solution(a, b):
    if a <= b and (a + b) % 2 == 0:
        return False
    else:
        return True


print(solution(users_a, users_b))
