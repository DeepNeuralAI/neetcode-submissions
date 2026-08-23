class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort(nums, 0, len(nums) - 1)
        return nums
    
    def sort(self, nums, l, r):
        if l >= r:
            return
        
        m = (l + r) // 2
        self.sort(nums, l, m)
        self.sort(nums, m + 1, r)
        self.merge(nums, l, m, r)

    def merge(self, nums, l, m, r):
        i = l
        j = m + 1
        res = []

        while i <= m and j <= r:
            if nums[i] <= nums[j]:
                res.append(nums[i])
                i += 1
            else:
                res.append(nums[j])
                j += 1
        
        while i <= m:
            res.append(nums[i])
            i += 1
        
        while j <= r:
            res.append(nums[j])
            j += 1
        
        for k in range(l, r + 1):
            nums[k] = res[k - l]
        
