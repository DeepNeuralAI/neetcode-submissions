class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l = 0
        r = k

        def compare(a, b, x):
            if abs(a - x) <= abs(b - x) and a < b:
                return 0
            return 1

        while l < n - k:
            r = l + k
            
            if compare(arr[l], arr[r], x) == 0:
                return arr[l : r]
            
            l += 1
            r += 1
        
        return arr[l: r]
        
        