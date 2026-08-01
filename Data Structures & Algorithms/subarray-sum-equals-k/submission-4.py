class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0 : 1}
        total = 0
        curSum = 0
        
        for num in nums:
            curSum += num
            total += count.get(curSum - k, 0)
            
            count[curSum] = count.get(curSum, 0) + 1
        
        return total





        