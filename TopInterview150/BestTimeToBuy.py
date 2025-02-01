#Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min:
                min = price
            else:
                max_profit = max(max_profit, price - min)
        return max_profit
    