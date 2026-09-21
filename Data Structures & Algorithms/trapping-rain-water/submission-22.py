class Solution:
    def trap(self, height: List[int]) -> int:
        # Greedily take the smaller height seen?
        n = len(height)
        left_max = right_max = 0
        l = 0
        r = n - 1


        total = 0
        while l <= r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max <= right_max:
                total += left_max - height[l]
                l += 1
            else:
                total += right_max - height[r]
                r -= 1
        return total

        
        