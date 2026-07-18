class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # N^2 Solution with Sorting
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                candidate = nums[i] + nums[j] + nums[k]
                if candidate == 0:
                    res.append([nums[i], nums[j], nums[k]])
                
                    j += 1
                    k -= 1
                    
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif candidate < 0:
                    j += 1
                else:
                    k -= 1
        return res



                        
        