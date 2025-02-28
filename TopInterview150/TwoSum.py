#Two sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
    
        # Recorremos el arreglo
        for i, num in enumerate(nums):
            complement = target - num
            
            # Verificamos si el complemento ya está en el hash map
            if complement in map:
                return [map[complement], i]  # Devolvemos los índices
            
            map[num] = i
        
        return []