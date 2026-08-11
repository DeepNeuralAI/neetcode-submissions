class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []

        def dfs(i):
            res.append(current.copy())

            for start in range(i, len(nums)):
                current.append(nums[start])
                dfs(start + 1)
                current.pop()
            
        dfs(0)
        return res

    

