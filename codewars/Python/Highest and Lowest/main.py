"""
7 kyu: Highest and Lowest
Kata: https://www.codewars.com/kata/554b4ac871d6813a03000035/
"""


def high_and_low(numbers: str) -> str:
    numbers = tuple(map(int, numbers.split(" ")))
    
    return "{} {}".format(
        max(numbers),
        min(numbers),
    )
