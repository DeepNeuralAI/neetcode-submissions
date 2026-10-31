from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # Greedy - Breadth First Search (Graph??)
        # Watch lesson
        res = 0
        l = r = 0


        while r < n - 1:
            farthest = r
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            
            res += 1
            l = r + 1
            r = farthest
        
        return res
        



       
        