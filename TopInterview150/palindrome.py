#Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filtrar los caracteres alfanuméricos y convertir a minúsculas
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        
        # Unir los caracteres filtrados en una cadena
        filtered_string = ''.join(filtered_chars)
        
        # Comparar la cadena filtrada con su reverso
        return filtered_string == filtered_string[::-1]
# Crear una instancia de la clase Solution
sol = Solution()

# Llamar al método isPalindrome con diferentes cadenas
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome(" "))  