class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0

        for i in range(n):
            for j in range(i + 1, n):
                height = min(heights[i], heights[j])
                width = j - i
                maxArea = max(maxArea, height * width)
        return maxArea

        