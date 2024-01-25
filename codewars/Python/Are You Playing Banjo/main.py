"""
8 kyu: Are You Playing Banjo?
Kata: https://www.codewars.com/kata/53af2b8861023f1d88000832/
"""


def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"

    return name + " does not play banjo"
