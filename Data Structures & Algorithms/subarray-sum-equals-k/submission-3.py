class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0 : 1}
        res = 0
        curSum = 0
        
        for num in nums:
            curSum += num
            if (curSum - k) in count:
                res += count[curSum - k]

            count[curSum] = count.get(curSum, 0) + 1
        
        return res
        