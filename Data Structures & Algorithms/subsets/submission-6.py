class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr, res = [], []
    
        def dfs(start):
            res.append(curr.copy())

            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(i + 1)
                curr.pop()
        
        dfs(0)
        return res
        