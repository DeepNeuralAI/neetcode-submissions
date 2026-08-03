class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        res = []
        self.dfs(nums, [], res, count)
        return res


    def dfs(self, nums, current, res, count):
        if len(current) == len(nums):
            res.append(current.copy())
            return
        
        for num in count:
            if count[num] > 0:
                current.append(num)
                count[num] -= 1

                self.dfs(nums, current, res, count)
                current.pop()
                count[num] += 1
        
        
        


