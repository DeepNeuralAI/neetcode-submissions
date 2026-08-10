class Solution:
    def trap(self, height: List[int]) -> int:
        # Two Pointers
        n = len(height)
        l = 0
        r = n - 1
        
        leftMaxSeen = height[l]
        rightMaxSeen = height[r]
        total = 0


        while l < r:
            if leftMaxSeen <= rightMaxSeen:
                l += 1
                total += max(0, leftMaxSeen - height[l])
                leftMaxSeen = max(leftMaxSeen, height[l])
            else:
                r -= 1
                total += max(0, rightMaxSeen - height[r])
                rightMaxSeen = max(rightMaxSeen, height[r])

        
        return total
            
            


            

        