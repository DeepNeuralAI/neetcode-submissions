class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer Moore

        required = len(nums) / 3
        cnt1 = 0
        cnt2 = 0

        el1 = None
        el2 = None

        for num in nums:
            if cnt1 == 0 and num != el2:
                el1 = num
                cnt1 += 1
            elif cnt2 == 0 and num != el1:
                el2 = num
                cnt2 += 1
            elif num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
        
        res = []
        if cnt1 > required:
            res.append(el1)
        
        if cnt2 > required:
            res.append(el2)
        
        return res
