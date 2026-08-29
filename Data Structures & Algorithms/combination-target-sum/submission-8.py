class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i, curr, subset):
            if curr == 0:
                res.append(subset.copy())
                return
            
            if i == len(nums) or curr < 0:
                return
            
            for start in range(i, len(nums)):
                if curr >= nums[start]:
                    subset.append(nums[start])
                    
                    dfs(start, curr - nums[start], subset)

                    subset.pop()
                   
        
        res = []
        dfs(0, target, [])
        return res
