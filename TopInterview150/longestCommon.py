#14. Longest Common Prefix

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest_str = min(strs, key=len)
        
        for i, char in enumerate(shortest_str):
            for string in strs:
                if string[i] != char:
                    return shortest_str[:i]
        return shortest_str   