"""
8 kyu: Counting sheep...
Kata: https://www.codewars.com/kata/54edbc7200b811e956000556/
"""


from typing import List


def count_sheeps(sheep: List[bool]) -> int:
    # If none of sheep are missing
    if all(sheep):
        return len(sheep)

    # If all of sheep are missing
    if not any(sheep):
        return 0

    sheep_counter = 0
    for one_sheep in sheep:
        if one_sheep:
            sheep_counter += 1

    return sheep_counter
