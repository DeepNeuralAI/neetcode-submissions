class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = 0
        n = len(nums)
        seen = set()

        for num in nums:
            seen.add(num)
        
        sorted_nums = sorted(seen)
        k = len(sorted_nums)

        for i in range(k):
            nums[i] = sorted_nums[i]
        
        return k


        