class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = 0
        n = len(height)

        l = 0
        r = n - 1
        total = 0

        while l <= r:
            if left_max <= right_max:
                left_max = max(left_max, height[l])
                total += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                total += right_max - height[r]
                r -= 1
        
        return total
        