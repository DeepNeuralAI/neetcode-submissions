class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        
        for i in nums:
            res = res | (1 << i)
        
        for i in range(n):
            if not (1 << i) & res:
                return i
        
        return n
        

        