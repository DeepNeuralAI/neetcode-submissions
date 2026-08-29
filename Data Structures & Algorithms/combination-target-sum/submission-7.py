class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i, curr, subset):
            if curr == 0:
                res.append(subset.copy())
                return
            
            for start in range(i, len(nums)):
                if curr >= nums[start]:
                    subset.append(nums[start])
                    curr -= nums[start]
                    
                    dfs(start, curr, subset)

                    subset.pop()
                    curr += nums[start]
        
        res = []
        dfs(0, target, [])
        return res
