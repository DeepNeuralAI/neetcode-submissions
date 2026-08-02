class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Search Space - Start of window of size k
        n = len(arr)
        l = 0
        r = n - k


        while l < r:
            m = (l + r) // 2

            if abs(arr[m] - x) <= abs(arr[m + k] - x):
                r = m
            else:
                l = m + 1
            
        return arr[l : l + k]

