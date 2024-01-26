"""
7 kyu: Bingo ( Or Not )
Kata: https://www.codewars.com/kata/5a1ee4dfffe75f0fcb000145/
"""


from typing import List


BINGO = set("BINGO")  # "BINGO" letters


def int_to_char(order: int) -> str:
    return chr(ord("A") + order - 1)


def bingo(array: List[int]) -> str:
    char_sequence = set(map(int_to_char, array))

    return "WIN" if BINGO.issubset(char_sequence) else "LOSE"
