class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking

        def backtrack(i):
            res.append(curr.copy())

            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(j + 1)
                curr.pop()
                # backtrack(j + 1)
            
        res, curr = [], []
        backtrack(0)
        return res
