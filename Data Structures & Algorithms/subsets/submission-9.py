class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr, res = [], []
        
        def backtrack(curr, i):
            res.append(curr.copy())

            for start in range(i, len(nums)):
                curr.append(nums[start])
                backtrack(curr, start + 1)
                curr.pop()
            
        backtrack(curr, 0)
        return res

        