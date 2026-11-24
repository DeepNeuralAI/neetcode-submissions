class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)

        for i in range(1, n + 1):
            xor ^= i
            xor ^= nums[i - 1]
        
        return xor


        

        