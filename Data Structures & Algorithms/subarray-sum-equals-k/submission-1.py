class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum_to_count = {0: 1}
        curSum = 0
        count = 0

        for i in range(n):
            curSum += nums[i]

            if curSum - k in sum_to_count:
                count += sum_to_count[curSum - k]
            
    
            sum_to_count[curSum] = sum_to_count.get(curSum, 0) + 1
        
        return count
            



        


        