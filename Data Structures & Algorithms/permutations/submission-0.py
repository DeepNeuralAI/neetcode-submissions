class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res


    def dfs(self, nums, current, res):
        if len(current) == len(nums):
            res.append(current.copy())
            return
    

        for num in nums:
            if num in current:
                continue
            
            current.append(num)
            self.dfs(nums, current, res)
            current.pop()
        
            

