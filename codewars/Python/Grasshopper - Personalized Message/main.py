"""
8 kyu: Grasshopper - Personalized Message
Kata: https://www.codewars.com/kata/5772da22b89313a4d50012f7/
"""


def greet(name: str, owner: str) -> str:
    return  "Hello boss" if name == owner else "Hello guest"
