class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0

        n = len(height)
        
        leftMax = height[0]
        rightMax = height[n - 1]

        l = 0
        r = n - 1
        res = 0

        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res




        