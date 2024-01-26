"""
6 kyu: Tribonacci Sequence
Kata: https://www.codewars.com/kata/556deca17c58da83c00002db/
"""


from typing import List


def tribonacci(sequence: List[int], n: int) -> List[int]:
    while len(sequence) < n:
        sequence.append(sum(sequence[-3:]))

    return sequence[:n]
