"""
8 kyu: Beginner - Reduce but Grow
Kata: https://www.codewars.com/kata/57f780909f7e8e3183000078/
"""


from functools import reduce
from typing import List


def grow(array: List[int]) -> int:
    return reduce(lambda a, b: a * b, array)
