class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result, i = 0, 0
        length = len(s)

        while i < length:
            if (i + 1 < length) and (s[i + 1] in roman) and (roman[s[i + 1]] > roman[s[i]]):
                result += roman[s[i + 1]] - roman[s[i]]
                i += 2
            else:
                result += roman[s[i]]
                i += 1
        
        return result
