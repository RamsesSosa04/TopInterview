class Solution:
    def isPalindrome(self, s: str) -> bool:
    filtered_chars = [char.lower() for char in s if char.isalnum()]
    
    # Unir los caracteres filtrados en una cadena
    filtered_string = ''.join(filtered_chars)
    
    # Comparar la cadena filtrada con su reverso
    return filtered_string == filtered_string[::-1]