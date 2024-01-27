"""
6 kyu: Pokemon Damage Calculator
Kata: https://www.codewars.com/kata/536e9a7973130a06eb000e9f/
"""


def calculate_effectiveness(attacker: str, defender: str) -> int:
    effectiveness = {
        "fire":     {"fire": 0.5, "water": 0.5, "grass": 2.0, "electric": 1.0},
        "water":    {"fire": 2.0, "water": 0.5, "grass": 0.5, "electric": 0.5},
        "grass":    {"fire": 0.5, "water": 2.0, "grass": 0.5, "electric": 1.0},
        "electric": {"fire": 1.0, "water": 2.0, "grass": 1.0, "electric": 0.5},
    }

    return effectiveness[attacker][defender]


def calculate_damage(attacker: str, defender: str, attack: int, defense: int) -> float:
    effectiveness = calculate_effectiveness(attacker, defender)
    damage = 50 * (attack / defense) * effectiveness

    return damage
