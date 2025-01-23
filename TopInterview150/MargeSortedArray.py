class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m-1
        p2 = n-1
        p = m + n - 1