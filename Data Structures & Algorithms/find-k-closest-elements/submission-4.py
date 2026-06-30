class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l = 0
        r = n - k

        # Iterating over start points for window of size k!

        while l < r:
            mid = (l + r) // 2

            if abs(x - arr[mid]) > abs(x - arr[mid + k]):
                # Left end point of window 1 and new right end point of window 2
                l = mid + 1
            else:
                r = mid
        return arr[l: l + k]
