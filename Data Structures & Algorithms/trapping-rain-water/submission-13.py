class Solution:
    def trap(self, height: List[int]) -> int:
        # Brute Force
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        for i in range(1, n):
            j = n - i - 1
            leftMax[i] = max(leftMax[i - 1], height[i - 1])
            rightMax[j] = max(rightMax[j + 1], height[j + 1])
        
        total = 0
        for i in range(n):
            water = max(0, min(leftMax[i], rightMax[i]) - height[i])
            total += water
        
        return total


            

        