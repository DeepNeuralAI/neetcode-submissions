class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        maxArea = 0
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                idx = stack.pop()
                nse = i
                pse = stack[-1] if stack else -1
                area = (nse - pse - 1) * heights[idx]
                maxArea = max(maxArea, area)

            stack.append(i)
        
        while stack:
            idx = stack.pop()
            pse = stack[-1] if stack else -1
            nse = n
            area = (nse - pse - 1) * heights[idx]
            maxArea = max(area, maxArea)
        
        return maxArea
    

    def findPSE(self, nums):
        n = len(nums)
        pse = [-1] * n

        stack = [0]
        
        for i in range(1, n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            if stack:
                pse[i] = stack[-1]
            
            stack.append(i)
        
        return pse

    def findNSE(self, nums):
        n = len(nums)
        nse = [n] * n
        stack = [n - 1]

        for i in range(n - 2, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]

            stack.append(i)
        
        return nse



