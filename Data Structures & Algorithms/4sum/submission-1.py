class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Hash Map Approach
        n = len(nums)
        ans = set()

        for i in range(n):
            for j in range(i + 1, n):
                seen = set()
                for k in range(j + 1, n):
                        candidate = nums[i] + nums[j] + nums[k]
                        need = target - candidate

                        if need in seen:
                            quad = [nums[i], nums[j], nums[k], need]
                            quad.sort()
                            ans.add(tuple(quad))
                        
                        seen.add(nums[k])
        
        return [list(q) for q in ans]

        