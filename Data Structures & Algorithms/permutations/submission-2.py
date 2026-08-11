class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr, res = [], []
        used = [False] * len(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                    
                used[i] = True
                curr.append(nums[i])

                backtrack(curr)

                used[i] = False
                curr.pop()
        
        backtrack(curr)
        return res
        

