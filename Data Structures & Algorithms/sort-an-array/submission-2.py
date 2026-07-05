class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.sort(nums, 0, n - 1)
        return nums

    def merge(self, nums, l, m, r):
        i = l
        j = m + 1
        merged = []

        while i <= m and j <= r:
            if nums[i] <= nums[j]:
                merged.append(nums[i])
                i += 1
            else:
                merged.append(nums[j])
                j += 1

        while i <= m:
            merged.append(nums[i])
            i += 1
        
        while j <= r:
            merged.append(nums[j])
            j += 1
        

        for i in range(l, r + 1):
            nums[i] = merged[i - l]
        

    def sort(self, nums, l, r):
        if l >= r:
            return
        
        m = (l + r) // 2
        self.sort(nums, l, m)
        self.sort(nums, m + 1, r)
        self.merge(nums, l, m, r)
        