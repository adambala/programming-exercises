"""
4 kyu: The observed PIN
Kata: https://www.codewars.com/kata/5263c6999e0f40dee200059d/
"""

from itertools import product
from typing import List


def get_pins(observed: str) -> List[str]:
    digit_variations = {
        "0": "08",
        "1": "124",
        "2": "2153",
        "3": "326",
        "4": "4157",
        "5": "52468",
        "6": "6359",
        "7": "748",
        "8": "85790",
        "9": "968",
    }

    combinations = product(*(digit_variations[digit] for digit in observed))

    return ["".join(combination) for combination in combinations]
