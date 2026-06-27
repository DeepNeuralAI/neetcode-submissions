class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Hash Map Approach
        ans = set()
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i + 1, n):
                curSum = nums[i] + nums[j]
                need = -curSum

                if need in seen:
                    triplet = [nums[i], nums[j], need]
                    triplet.sort()
                    ans.add(tuple(triplet))
                
                seen.add(nums[j])

        return [list(t) for t in ans]
                



        