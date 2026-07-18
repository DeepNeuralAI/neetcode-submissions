class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        l = 0
        r = n - 1
        maxArea = 0

        while l < r:
            if heights[l] <= heights[r]:
                maxArea = max(maxArea, heights[l] * (r - l))
                l += 1
            else:
                maxArea = max(maxArea, heights[r] * (r - l))
                r -= 1
        return maxArea


                



        