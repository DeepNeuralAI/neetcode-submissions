class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Brute Force
        num_to_freq = {}
        ans = []
        n = len(nums)

        for num in nums:
            num_to_freq[num] = num_to_freq.get(num, 0) + 1

            if num_to_freq[num] > n / 3 and num not in ans:
                ans.append(num)
        
        return ans
        