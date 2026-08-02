class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_max = 0
        l = 0
        n = len(heights)
        r = n - 1

        # Area: (r - l) * min(heights[l], heights[r])

        while l <= r:
            if heights[l] <= heights[r]:
                current_area = (r - l) * heights[l]
                l += 1
            else:
                current_area = (r - l) * heights[r]
                r -= 1
            
            current_max = max(current_max, current_area)
        
        return current_max
        