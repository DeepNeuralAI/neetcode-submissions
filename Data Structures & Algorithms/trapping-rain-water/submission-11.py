class Solution:
    def trap(self, height: List[int]) -> int:
        lMax = rMax = 0
        n = len(height)

        l = 0
        r = n - 1
        total = 0

        while l < r:
            if height[l] <= height[r]:
                if lMax >= height[l]:
                    total += (lMax - height[l])
                lMax = max(height[l], lMax)
                l += 1
            else:
                if rMax >= height[r]:
                    total += (rMax - height[r])
                rMax = max(height[r], rMax)
                r -= 1

        return total
