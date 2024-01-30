"""
8 kyu: DNA to RNA Conversion
Kata: https://www.codewars.com/kata/5556282156230d0e5e000089/
"""


def dna_to_rna(dna: str) -> str:
    return dna.replace("T", "U")
