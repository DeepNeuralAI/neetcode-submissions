class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0 : 1}
        n = len(nums)

        curr_sum = 0
        total = 0
        
        for i in range(n):
            curr_sum += nums[i]

            if curr_sum - k in count:
                total += count[curr_sum - k]
    
            count[curr_sum] = count.get(curr_sum, 0) + 1
        return total


        