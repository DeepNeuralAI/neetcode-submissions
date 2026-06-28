class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two Pointers
        n = len(heights)
        l = 0
        r = n - 1
        curMax = 0

        while l < r:
            h = min(heights[r], heights[l])
            w = r - l
            curMax = max(h * w, curMax)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return curMax
        


        