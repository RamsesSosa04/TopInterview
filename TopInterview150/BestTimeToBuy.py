class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')  # Inicializamos con infinito para encontrar el mínimo
        max_profit = 0  # Beneficio máximo inicializado en 0

        for price in prices:
            if price < min_price:
                min_price = price  # Actualizamos el precio mínimo si encontramos uno menor
            else:
                max_profit = max(max_profit, price - min_price)  # Calculamos la ganancia si vendemos hoy

        return max_profit  # Retornamos la máxima ganancia posible