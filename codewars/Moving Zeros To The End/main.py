"""
5 kyu: Moving Zeros To The End
Kata: https://www.codewars.com/kata/52597aa56021e91c93000cb0/
"""


def move_zeros(lst):
    non_zeros, zeros, = [], []

    for element in lst:
        if element:
            non_zeros.append(element)
        else:
            zeros.append(element)

    non_zeros.extend(zeros)

    return non_zeros
