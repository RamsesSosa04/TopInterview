#Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_chars = [char.lower() for char in s if char.isalnum()]
        
        filtered_string = ''.join(filtered_chars)
        return filtered_string == filtered_string[::-1]
sol = Solution()
print(sol.isPalindrome("windows"))  