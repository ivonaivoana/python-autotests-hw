"""
Calculate the sum of the digits of hours and minutes from a given number n (total minutes).

Example:
Input: 75 -> 1 hour, 15 minutes -> digits 1, 1, 5 -> sum 7
"""

n = int(input('Enter the n value: '))
print(sum(int(x) for x in (list(str(n // 60)) + list(str(n % 60)))))
