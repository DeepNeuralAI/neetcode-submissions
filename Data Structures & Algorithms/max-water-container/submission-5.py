class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        l = 0
        r = n - 1
        maxArea = 0

        while l < r:
            height = min(heights[l], heights[r])
            maxArea = max(maxArea, height * (r - l))       

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1        
        return maxArea


                



        