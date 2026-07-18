class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = rightMax = 0
        n = len(height)

        l = 0
        r = n - 1
        total = 0

        while l < r:
            if height[l] <= height[r]:
                total += max(0, leftMax - height[l])
                leftMax = max(leftMax, height[l])
                l += 1
            else:
                total += max(0, rightMax - height[r])
                rightMax = max(rightMax, height[r])
                r -= 1
        return total

        