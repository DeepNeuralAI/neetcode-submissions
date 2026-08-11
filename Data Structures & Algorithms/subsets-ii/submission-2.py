class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        curr, res = [], []
        n = len(nums)
        
        def backtrack(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()

            start = i + 1
            while start < n and nums[start - 1] == nums[start]:
                start += 1
            
            backtrack(start)


        backtrack(0)
        return res


        