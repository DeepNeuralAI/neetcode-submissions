class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Using Modified Boyer Moore
        n = len(nums)
        cnt0 = cnt1 = 0
        candidate0 = candidate1 = None, None

        for num in nums:
            if cnt0 == 0 and num != candidate1:
                candidate0 = num
                cnt0 = 1
            elif cnt1 == 0 and num != candidate0:
                candidate1 = num
                cnt1 = 1
            elif num == candidate0:
                cnt0 += 1
            elif num == candidate1:
                cnt1 += 1
            else:
                cnt0 -= 1
                cnt1 -= 1
        
        cnt0 = cnt1 = 0
        for num in nums:
            if num == candidate0:
                cnt0 += 1
            elif num == candidate1:
                cnt1 += 1
        
        ans = []
        if cnt0 > n / 3:
            ans.append(candidate0)
        
        if cnt1 > n / 3:
            ans.append(candidate1)
        
        return ans