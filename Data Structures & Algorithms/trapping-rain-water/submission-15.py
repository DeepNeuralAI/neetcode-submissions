class Solution:
    def trap(self, height: List[int]) -> int:
        # Two Pointers
        n = len(height)
        leftMaxSeen = 0
        rightMaxSeen = 0
        total = 0

        l = 0
        r = n - 1

        while l <= r:
            if height[l] <= height[r]:
                leftMaxSeen = max(leftMaxSeen, height[l])
                total += leftMaxSeen - height[l]
                l += 1
            else:
                rightMaxSeen = max(rightMaxSeen, height[r])
                total += rightMaxSeen - height[r]
                r -= 1
        return total
            
            


            

        