class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": -2,
            "IX": -2,
            "XL": -20,
            "XC": -20,
            "CD": -200,
            "CM": -200,
        }
        sum = 0
        for symbol, val in mapping.items():
            sum += s.count(symbol) * val
        return sum