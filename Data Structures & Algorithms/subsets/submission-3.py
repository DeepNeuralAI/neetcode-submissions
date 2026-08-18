class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr, res = [], []
        
        def backtrack(start):
            res.append(curr.copy())

            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1)
                curr.pop()
        
        backtrack(0)
        return res
        