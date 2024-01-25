"""
6 kyu: Duplicate Encoder
Kata: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/
"""


from collections import Counter


def duplicate_encode(word):
    word = word.lower()
    word_dict = Counter(word)  # letter appearence count

    result = ''
    for letter in word:
        if word_dict[letter] > 1:
            result += ')'
        else:
            result += '('

    return result
