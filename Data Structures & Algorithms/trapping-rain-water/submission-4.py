class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        maxLeft = 0
        maxRight = 0
        res = 0

        while l < r:
            if height[l] <= height[r]:
                res += max(0, maxLeft - height[l])
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                res += max(0, maxRight - height[r])
                maxRight = max(maxRight, height[r])
                r -= 1
        return res
                