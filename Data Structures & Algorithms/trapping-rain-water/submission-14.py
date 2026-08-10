class Solution:
    def trap(self, height: List[int]) -> int:
        # Brute Force
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        rightMax[n - 1] = height[n - 1]

        for i in range(1, n):
            j = n - 1 - i
            leftMax[i] = max(leftMax[i - 1], height[i])
            rightMax[j] = max(rightMax[j + 1], height[j])
        
        total = 0
        for i in range(n):
            water = max(0, min(leftMax[i], rightMax[i]) - height[i])
            total += water
        
        return total


            

        