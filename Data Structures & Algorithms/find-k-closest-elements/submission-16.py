class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Search Space - starting position for window of size k
        n = len(arr)

        l = 0
        r = n - k


        while l < r:
            mid = (l + r) // 2

            if abs(arr[mid] - x) > abs(arr[mid + k] - x):
                l = mid + 1
            else:
                r = mid
        
        return arr[l : l + k]

            


        