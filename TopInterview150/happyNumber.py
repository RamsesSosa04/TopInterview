#Happy number
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sum_of_squares(number):
            total = 0
            while number > 0:
                digit = number % 10
                total += digit ** 2
                number //= 10
