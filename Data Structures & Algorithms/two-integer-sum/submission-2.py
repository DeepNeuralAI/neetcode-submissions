class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Modify / Sorted
        n = len(nums)
        nums_sorted = [(nums[i], i) for i in range(n)]
        nums_sorted.sort()

        i = 0
        j = n - 1

        while i < j:
            candidate = nums_sorted[i][0] + nums_sorted[j][0]
            if candidate == target:
                return sorted([nums_sorted[i][1], nums_sorted[j][1]])
            
            if candidate < target:
                i += 1
            else:
                j -= 1
        return [-1, -1]
            



        