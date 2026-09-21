class Solution:
    def trap(self, height: List[int]) -> int:
        # Pre-compute leftMax and rightMax
        n = len(height)
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        leftMax[0] = height[0]
        rightMax[n - 1] = height[n - 1]

        for i in range(1, len(height)):
            leftMax[i] = max(height[i], leftMax[i - 1])
        
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i + 1])
        
        water = 0
        for i in range(n):
            water += min(leftMax[i], rightMax[i]) - height[i]
        
        return water
        