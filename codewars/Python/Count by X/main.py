"""
8 kyu: Count by X
Kata: https://www.codewars.com/kata/5513795bd3fafb56c200049e/
"""


def count_by(x: int, n: int) -> int:
    """Return a sequence of numbers counting by `x` `n` times."""
    return [i*x for i in range(1, n + 1)]
