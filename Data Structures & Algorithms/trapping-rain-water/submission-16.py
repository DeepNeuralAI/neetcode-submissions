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
            if leftMaxSeen <= rightMaxSeen:
                water = max(0, leftMaxSeen - height[l])
                leftMaxSeen = max(leftMaxSeen, height[l])
                l += 1
            else:
                water = max(0, rightMaxSeen - height[r])
                rightMaxSeen = max(rightMaxSeen, height[r])
                r -= 1
            total += water
        
        return total
            
            


            

        