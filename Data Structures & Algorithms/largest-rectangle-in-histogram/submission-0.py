class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pse = self.findPSE(heights)
        nse = self.findNSE(heights)

        maxArea = 0
        for i in range(n):
            width = (nse[i] - pse[i] - 1) 
            maxArea = max(maxArea, width * heights[i])
        
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



