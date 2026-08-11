class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr, res = [], []
        used = [False] * len(nums)
        
        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if not used[i - 1] and (i > 0 and nums[i] == nums[i - 1]):
                    continue

                # Choose
                used[i] = True
                curr.append(nums[i])
                
                backtrack()
                
                # Undo choice
                used[i] = False
                curr.pop()
        
        backtrack()
        return res

        
   