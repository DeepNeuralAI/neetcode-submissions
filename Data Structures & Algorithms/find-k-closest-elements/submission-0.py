class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ansStart = 0
        ansEnd = k - 1
        
        diff = 0
        for i in range(k):
            diff += abs(arr[i] - x)
        
        res = diff
        
        l = 0
        r = k
        while r < len(arr):
            diff += abs(arr[r] - x)
            diff -= abs(arr[l] - x)
            l += 1

            if diff < res:
                res = diff
                ansStart = l
                ansEnd = r
            
            r += 1
        
        return arr[ansStart : ansEnd + 1]
