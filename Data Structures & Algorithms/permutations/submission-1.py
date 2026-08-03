class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)
        self.dfs(nums, [], res, visited)
        return res


    def dfs(self, nums, current, res, visited):
        if len(current) == len(nums):
            res.append(current.copy())
            return
    

        for i in range(len(nums)):
            if not visited[i]:
                current.append(nums[i])
                visited[i] = True
                self.dfs(nums, current, res, visited)
                current.pop()
                visited[i] = False
            
        
            

