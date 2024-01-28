"""
8 kyu: Find Maximum and Minimum Values of a List
Kata: https://www.codewars.com/kata/577a98a6ae28071780000989/
"""


from typing import List


def minimum(array: List[int]) -> int:
    min_number = array[0]

    for number in array[1:]:
        if number < min_number:
            min_number = number

    return min_number


def maximum(array: List[int]) -> int:
    max_number = array[0]

    for number in array[1:]:
        if max_number < number:
            max_number = number

    return max_number
