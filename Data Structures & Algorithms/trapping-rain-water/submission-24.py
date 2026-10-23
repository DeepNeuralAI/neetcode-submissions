class Solution:
    def trap(self, height: List[int]) -> int:
        # Invariant
        # Amount of trapped water: water[i] = min(left_max, right_max) - height[i]
        # Keep track of current left_max and right_max
        # Two pointer approach: 0 and n - 1 starting points for l and r
        left_max = right_max = water = 0
        n = len(height)
        l = 0
        r = n - 1

        while l <= r:
            left_max = max(height[l], left_max)
            right_max = max(height[r], right_max)

            if left_max <= right_max:
                water += left_max - height[l]
                l += 1
            else:
                water += right_max - height[r]
                r -= 1
        
        return water
            


        