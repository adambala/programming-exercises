"""
7 kyu: Isograms
Kata: https://www.codewars.com/kata/54ba84be607a92aa900000f1/
"""


def is_isogram(string: str) -> bool:
    characters = set(string.lower())

    return len(characters) == len(string)
