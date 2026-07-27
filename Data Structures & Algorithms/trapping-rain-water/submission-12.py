class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lMax = 0
        rMax = 0

        l = 0
        r = n - 1
        total = 0

        while l <= r:
            if lMax <= rMax:
                lMax = max(lMax, height[l])
                total += lMax - height[l]
                l += 1
            else:

                rMax = max(rMax, height[r])
                total += rMax - height[r]
                r -= 1

        return total
