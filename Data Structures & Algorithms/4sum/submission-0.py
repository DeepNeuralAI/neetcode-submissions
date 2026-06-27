class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Brute Force
        n = len(nums)
        ans = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        candidate = nums[i] + nums[j] + nums[k] + nums[l]

                        if candidate == target:
                            quad = [nums[i], nums[j], nums[k], nums[l]]
                            quad.sort()
                            ans.add(tuple(quad))
        
        return [list(q) for q in ans]

        