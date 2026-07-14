class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0

        while l < r:
            if heights[l] <= heights[r]:
                res = max((r - l) * heights[l], res)
                l += 1
            else:
                res = max((r - l) * heights[r], res)
                r -= 1
        
        return res

        