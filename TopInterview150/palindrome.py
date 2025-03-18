#Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        
        filtered_string = ''.join(filtered_chars)
