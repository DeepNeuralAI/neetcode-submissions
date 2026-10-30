class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        n = len(nums)
        canReach = [False] * n
        canReach[n - 1] = True
        
        for i in range(n - 2, -1, -1):
            if nums[i] == 0:
                continue
            
            jumps = nums[i]
            for j in range(1, jumps + 1):
                if i + j >= n - 1:
                    canReach[i] = True
                    break

                if canReach[i + j]:
                    canReach[i] = True
                    break
            
        return canReach[0]



        