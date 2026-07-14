class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt0 = cnt1 = 0
        el1 = el2 = None

        for num in nums:
            if cnt0 == 0 and num != el2:
                el1 = num
                cnt0 = 1
            elif cnt1 == 0 and num != el1:
                el2 = num
                cnt1 = 1
            elif num == el1:
                cnt0 += 1
            elif num == el2:
                cnt1 += 1
            else:
                cnt0 -= 1
                cnt1 -= 1
        
        required = len(nums) / 3
        res = []
        if nums.count(el1) > required:
            res.append(el1)
        
        if nums.count(el2) > required:
            res.append(el2)
        
        return res
        