#Esta es una app para saber cual es la frase mas larga de la frase

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        word = s.split()
        return len(word[-1])
    