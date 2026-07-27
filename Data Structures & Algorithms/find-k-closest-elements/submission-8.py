class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        
        window_diff = 0
        for i in range(k):
            window_diff += abs(arr[i] - x)
        
        min_diff = window_diff
        ansStart = 0
        
        l = 0
        r = k

        while r < n:
            window_diff += abs(arr[r] - x)
            window_diff -= abs(arr[l] - x)
            l += 1

            if window_diff < min_diff:
                ansStart = l
                min_diff = window_diff

            r += 1
        
        return arr[ansStart : ansStart + k]

