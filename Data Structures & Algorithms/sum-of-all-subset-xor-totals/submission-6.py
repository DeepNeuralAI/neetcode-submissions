class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, total):
            if i == len(nums):
                return total

            left = dfs(i + 1, nums[i] ^ total)
            right = dfs(i + 1, total)

            return left + right

        return dfs(0, 0)  