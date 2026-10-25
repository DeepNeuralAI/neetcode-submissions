class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if not arr:
            return 0
        
        if n == 1:
            return 1
        
        prevDirection = 0
        if arr[1] > arr[0]:
            prevDirection = 1
        elif arr[1] < arr[0]:
            prevDirection = -1
        
        if prevDirection != 0:
            curLen = maxLen = 2
        else:
            curLen = maxLen = 1

        
        for i in range(2, n):
            curDirection = 0
            if arr[i] > arr[i - 1]:
                curDirection = 1
            elif arr[i] < arr[i - 1]:
                curDirection = -1
            
           
            # Current Direction -> 0
            if curDirection == 0:
                curLen = 1
            # Direction Alternates
            elif prevDirection == -curDirection:
                curLen += 1
            # Same Direction
            else:
                curLen = 2
            

            prevDirection = curDirection
            maxLen = max(maxLen, curLen)


        return maxLen

        
    
        