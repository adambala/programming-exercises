"""
6 kyu: Is a number prime?
Kata: https://www.codewars.com/kata/5262119038c0985a5b00029f/
"""


def is_prime(num):
    if num > 1:
        # It's useless to check all integers in [2, num], because
        # each divisor [2, sqrt(num)] has its own pair in [sqrt(num), num//2].
        sq = int(num**0.5)
        for k in range(2, sq + 1):
            if num % k == 0:
                return False
    else:
        return False

    return True
