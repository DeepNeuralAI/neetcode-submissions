class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        # Brute Force
        n = len(height)
        total = 0

        for i in range(n):
            leftMax = rightMax = 0

            for j in range(i):
                leftMax = max(leftMax, height[j])
            
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])
            
            currentMax = min(leftMax, rightMax)
            
            if currentMax > height[i]:
                total += currentMax - height[i]
            
        return total
