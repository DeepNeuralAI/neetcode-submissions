class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 1, n - 2
        maxLeft = height[0]
        maxRight = height[n - 1]
        total = 0

        while l <= r:
            if maxLeft <= maxRight:
                water = maxLeft - height[l]
                total += (0 if water < 0 else water)
        
                maxLeft = max(maxLeft, height[l])
                l += 1
                
            else:
                water = maxRight - height[r]
                total += (0 if water < 0 else water)
                
                maxRight = max(maxRight, height[r])
                r -= 1
                
        return total


