"""
7 kyu: Build a square
Kata: https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/
"""


def generate_shape(n: int) -> str:
    return "\n".join(["+" * n] * n)
