"""
5 kyu: Count IP Addresses
Kata: https://www.codewars.com/kata/526989a41034285187000de4/
"""


def ipv4_to_decimal(ipv4: str) -> int:
    octets = map(int, ipv4.split("."))
    binary = [f"{octet:08b}" for octet in octets]

    return int("".join(binary), 2)


def ips_between(start: str, end: str) -> int:
    return ipv4_to_decimal(end) - ipv4_to_decimal(start)
