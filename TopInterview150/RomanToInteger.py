#13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0 
        valor_anterior = 0
        
        for char in reversed(s):
            value = roman_to_int[char]
            if value < valor_anterior:
                total -= value
            else:
                total += value
            valor_anterior = value
        return total