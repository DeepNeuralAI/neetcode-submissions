class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt1 = cnt2 = 0
        el1 = el2 = None
        count_required = n / 3

        for num in nums:
            if cnt1 == 0 and el2 != num:
                el1 = num
                cnt1 = 1
            elif cnt2 == 0 and el1 != num:
                el2 = num
                cnt2 = 1
            elif el1 == num:
                cnt1 += 1
            elif el2 == num:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1 = cnt2 = 0
        res = []
        for num in nums:
            if num == el1:
                cnt1 += 1
            
            if num == el2:
                cnt2 += 1
        
        if cnt1 > count_required:
            res.append(el1)
        
        if cnt2 > count_required:
            res.append(el2)
        
        return res

            
            
        