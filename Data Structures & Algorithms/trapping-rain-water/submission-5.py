class Solution:
    def trap(self, height: List[int]) -> int:
        # Prefix and Suffix 
        n = len(height)

        leftMax = [0] * n
        rightMax = [0] * n

        for i in range(1, n):
            leftMax[i] = max(height[i - 1], leftMax[i - 1])
        
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(height[i + 1], rightMax[i + 1])
        
        total = 0
        for i in range(n):
            total += max(min(rightMax[i], leftMax[i]) - height[i], 0)
        return total
           
