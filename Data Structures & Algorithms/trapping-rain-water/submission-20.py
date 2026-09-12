class Solution:
    def trap(self, height: List[int]) -> int:
        # Two Pointers
        n = len(height)
        l = 0
        r = n - 1

        leftMax = height[0]
        rightMax = height[n - 1]
        water = 0
        
        while l <= r:
            if leftMax <= rightMax:
                water += max(0, leftMax - height[l])
                leftMax = max(leftMax, height[l])
                l += 1
            else:
                water += max(0, rightMax - height[r])
                rightMax = max(rightMax, height[r])
                r -= 1
        
        return water


            
            


            

        