"""
Kata: https://www.codewars.com/kata/5583090cbe83f4fd8c000051/
"""


from math import log10


def digitize(n):
    if n == 0:
        return [0]

    length = int(log10(n)) + 1 if n > 0 else 0
    digits = []

    for _ in range(length):
        digits.append(n % 10)
        n = n // 10

    return digits
