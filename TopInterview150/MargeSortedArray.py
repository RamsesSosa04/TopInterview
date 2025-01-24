from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Punteros iniciales
        p1 = m - 1  # Último índice válido de nums1
        p2 = n - 1  # Último índice de nums2
        p = m + n - 1  # Último índice total de nums1

        # Fusionar desde el final hacia el principio
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Si quedan elementos en nums2 (nums1 ya está en su lugar)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
