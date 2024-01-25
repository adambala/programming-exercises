"""
5 kyu: RGB To Hex Conversion
Kata: https://www.codewars.com/kata/513e08acc600c94f01000001/
"""


def rgb(r: int, g: int, b: int) -> str:
    """Convert RGB to Hex."""

    return "{:02X}{:02X}{:02X}".format(
        max(0, min(r, 255)),
        max(0, min(g, 255)),
        max(0, min(b, 255)),
    )
