class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Frequency Map
        n = len(nums)
        majority = n / 2
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1

            if freq[num] > majority:
                return num
        return -1

        