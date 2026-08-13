class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        curr, res = [], []
        
        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if used[i]: continue

                used[i] = True
                curr.append(nums[i])
                
                backtrack()
                
                curr.pop()
                used[i] = False  

        backtrack()
        return res 