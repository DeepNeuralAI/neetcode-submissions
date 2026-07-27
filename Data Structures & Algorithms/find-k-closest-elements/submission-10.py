class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        
        # Need to find starting index of window of size k
        # Search space (valid) is [0, n - k]
        l = 0
        r = n - k

        while l <= r:
            mid = (l + r) // 2

            # Start of window is arr[mid]
            # Element after window: arr[mid + k]

            current_dist = abs(arr[mid] - x)
            next_window_dist = abs(arr[mid + k] - x) if mid + k < n else float('inf')

            if current_dist <= next_window_dist:
                r = mid - 1
            else:
                l = mid + 1
        
        return arr[l : l + k]

