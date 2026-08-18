class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr, res = [], []
        
        def backtrack(start, target):
            if target == 0:
                res.append(curr.copy())
                return
            
            for i in range(start, len(nums)):
                if target - nums[i] >= 0:
                    curr.append(nums[i])
                    backtrack(i, target - nums[i])
                    curr.pop()
        
        backtrack(0, target)
        return res
                
            

        